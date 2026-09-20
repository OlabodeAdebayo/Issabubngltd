from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.viewsets import ModelViewSet
from .models import QuoteRequest
from .serializers import QuoteRequestSerializer

class QuoteRequestViewSet(ModelViewSet):
    queryset = QuoteRequest.objects.all().order_by('-created_at')
    serializer_class = QuoteRequestSerializer

    def get_permissions(self):
        return [AllowAny()] if self.action == 'create' else [IsAdminUser()]

    def get_throttles(self):
        if self.action == 'create':
            return [ScopedRateThrottle()]
        return super().get_throttles()

    throttle_scope = 'quotes'
