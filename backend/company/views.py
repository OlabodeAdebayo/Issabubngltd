from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import CompanyProfile
from .serializers import CompanyProfileSerializer
class CompanyProfileViewSet(ModelViewSet):
    queryset=CompanyProfile.objects.all().order_by('id');serializer_class=CompanyProfileSerializer
    def get_permissions(self): return [AllowAny()] if self.action in ('list','retrieve') else [IsAdminUser()]
