from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectSerializer
class ProjectViewSet(ModelViewSet):
    queryset=Project.objects.all();serializer_class=ProjectSerializer;lookup_field='slug'
    def get_permissions(self): return [AllowAny()] if self.action in ('list','retrieve') else [IsAdminUser()]
    def get_queryset(self):
        qs=Project.objects.all()
        category=self.request.query_params.get('category')
        if category in dict(Project.CATEGORY_CHOICES): qs=qs.filter(category=category)
        if self.request.query_params.get('featured')=='1': qs=qs.filter(featured=True)
        return qs
