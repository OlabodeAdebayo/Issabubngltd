import json
import logging
import threading
import urllib.error
import urllib.request

from django.conf import settings
from django.utils import timezone
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.viewsets import ModelViewSet

from .models import QuoteRequest
from .serializers import QuoteRequestSerializer

logger = logging.getLogger(__name__)


def send_quote_email(quote_id):
    quote = QuoteRequest.objects.filter(pk=quote_id).first()
    if not quote:
        return

    api_key = getattr(settings, "RESEND_API_KEY", "") or ""
    if not api_key:
        quote.email_sent = False
        quote.email_error = "RESEND_API_KEY is not configured."
        quote.save(update_fields=["email_sent", "email_error"])
        return

    to_email = getattr(
        settings,
        "QUOTE_NOTIFICATION_EMAIL",
        "issabubngltd@outlook.com",
    )
    from_email = getattr(
        settings,
        "RESEND_FROM_EMAIL",
        "ISSABUB Website <beth.t@example.com>",
    )

    text = f"""New website quote request

Full name: {quote.full_name}
Email: {quote.email}
Phone: {quote.phone}
Service: {quote.service}
Project location: {quote.project_location or "Not provided"}

Project details:
{quote.message}

Request ID: {quote.pk}
Submitted: {quote.created_at}
"""

    payload = json.dumps(
        {
            "from": from_email,
            "to": [to_email],
            "reply_to": quote.email,
            "subject": f"New Website Quote Request - {quote.service}",
            "text": text,
        }
    ).encode("utf-8")

    request = urllib.request.Request(
        "https://api.resend.com/emails",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=8) as response:
            response.read()
        quote.email_sent = True
        quote.email_sent_at = timezone.now()
        quote.email_error = ""
        quote.save(update_fields=["email_sent", "email_sent_at", "email_error"])
    except Exception as exc:
        logger.exception("Quote email failed")
        quote.email_sent = False
        quote.email_error = str(exc)
        quote.save(update_fields=["email_sent", "email_error"])


class QuoteRequestViewSet(ModelViewSet):
    queryset = QuoteRequest.objects.all().order_by("-created_at")
    serializer_class = QuoteRequestSerializer
    throttle_scope = "quotes"

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAdminUser()]

    def get_throttles(self):
        if self.action == "create":
            return [ScopedRateThrottle()]
        return super().get_throttles()

    def perform_create(self, serializer):
        quote = serializer.save()
        thread = threading.Thread(
            target=send_quote_email,
            args=(quote.pk,),
            daemon=True,
        )
        thread.start()
