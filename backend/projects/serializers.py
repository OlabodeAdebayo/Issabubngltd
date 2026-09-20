from rest_framework import serializers
from .models import Project
class ProjectSerializer(serializers.ModelSerializer):
    category_label=serializers.CharField(source='get_category_display',read_only=True)
    class Meta: model=Project;fields='__all__'
