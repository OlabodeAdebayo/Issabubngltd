from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','category','featured','created_at')
    list_filter = ('category','featured')
    search_fields = ('title','description','location')
    prepopulated_fields = {'slug': ('title',)}
