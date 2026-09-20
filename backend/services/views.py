from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import Service
from .serializers import ServiceSerializer
class ServiceViewSet(ModelViewSet):
    queryset=Service.objects.filter(active=True);serializer_class=ServiceSerializer;lookup_field='slug'
    def get_queryset(self): return Service.objects.all() if self.request.user.is_staff else Service.objects.filter(active=True)
    def get_permissions(self): return [AllowAny()] if self.action in ('list','retrieve') else [IsAdminUser()]
