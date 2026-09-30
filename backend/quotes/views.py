from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone

from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.viewsets import ModelViewSet

from .models import QuoteRequest
from .serializers import QuoteRequestSerializer


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

        if not getattr(settings, "EMAIL_HOST_PASSWORD", ""):
            quote.email_sent = False
            quote.email_error = "EMAIL_HOST_PASSWORD is not configured."
            quote.save(update_fields=["email_sent", "email_error"])
            return

        subject = f"New Website Quote Request - {quote.service}"

        body = f"""
ISSABUB NIGERIA LIMITED
NEW WEBSITE QUOTE REQUEST

========================================
CUSTOMER INFORMATION
========================================

Full Name:
{quote.full_name}

Email:
{quote.email}

Phone:
{quote.phone}

Requested Service:
{quote.service}

Project Location:
{quote.project_location or "Not provided"}

========================================
PROJECT / CUSTOMER MESSAGE
========================================

{quote.message}

========================================
REQUEST INFORMATION
========================================

Request ID:
{quote.pk}

Status:
{quote.get_status_display()}

Submitted:
{quote.created_at.strftime("%d %B %Y, %I:%M %p")}

========================================

This enquiry was submitted through the
ISSABUB Nigeria Limited website.
"""

        notification_email = getattr(
            settings,
            "QUOTE_NOTIFICATION_EMAIL",
            "issabubngltd@outlook.com",
        )

        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[notification_email],
            reply_to=[quote.email],
        )

        try:
            email.send(fail_silently=False)
            quote.email_sent = True
            quote.email_sent_at = timezone.now()
            quote.email_error = ""
            quote.save(update_fields=["email_sent", "email_sent_at", "email_error"])
        except Exception as exc:
            quote.email_sent = False
            quote.email_error = str(exc)
            quote.save(update_fields=["email_sent", "email_error"])
