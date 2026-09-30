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
        # Do not send email inside this request.
        # Railway cannot reliably reach Outlook SMTP, and a hung
        # smtp connect blocks the single gunicorn worker (500 + CORS).
        serializer.save()
