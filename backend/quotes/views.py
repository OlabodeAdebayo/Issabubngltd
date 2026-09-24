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

    def get_permissions(self):
        """
        Website visitors can create quote requests.

        Only authenticated Django administrators can:
        - list requests
        - retrieve requests
        - update requests
        - delete requests
        """

        if self.action == "create":
            return [AllowAny()]

        return [IsAdminUser()]

    def get_throttles(self):
        """
        Apply the quotes-specific rate limit to public submissions.
        """

        if self.action == "create":
            return [ScopedRateThrottle()]

        return super().get_throttles()

    throttle_scope = "quotes"

    def perform_create(self, serializer):
        """
        Save the quote request and send an email notification
        to ISSABUB Nigeria Limited.
        """

        # ---------------------------------------------------------
        # 1. Save the customer's quote request
        # ---------------------------------------------------------

        quote = serializer.save()

        # ---------------------------------------------------------
        # 2. Build email subject
        # ---------------------------------------------------------

        subject = (
            f"New Website Quote Request - "
            f"{quote.service}"
        )

        # ---------------------------------------------------------
        # 3. Build email body
        # ---------------------------------------------------------

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

        # ---------------------------------------------------------
        # 4. Get notification email from settings
        # ---------------------------------------------------------

        notification_email = getattr(
            settings,
            "QUOTE_NOTIFICATION_EMAIL",
            "issabubngltd@outlook.com"
        )

        # ---------------------------------------------------------
        # 5. Create email
        # ---------------------------------------------------------

        email = EmailMessage(
            subject=subject,

            body=body,

            from_email=settings.DEFAULT_FROM_EMAIL,

            to=[
                notification_email
            ],

            reply_to=[
                quote.email
            ],
        )

        # ---------------------------------------------------------
        # 6. Send email
        # ---------------------------------------------------------

        try:

            email.send(
                fail_silently=False
            )

            # -----------------------------------------------------
            # 7. Record successful email delivery attempt
            # -----------------------------------------------------

            quote.email_sent = True

            quote.email_sent_at = timezone.now()

            quote.email_error = ""

            quote.save(
                update_fields=[
                    "email_sent",
                    "email_sent_at",
                    "email_error",
                ]
            )

        except Exception as exc:

            # -----------------------------------------------------
            # 8. Record email failure
            # -----------------------------------------------------

            quote.email_sent = False

            quote.email_error = str(exc)

            quote.save(
                update_fields=[
                    "email_sent",
                    "email_error",
                ]
            )

            # Do NOT delete the quote.
            #
            # The customer's request is still safely stored
            # in the database.
