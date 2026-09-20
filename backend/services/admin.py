from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('number','title','active','created_at')
    list_filter = ('active',)
    search_fields = ('title','description','applications')
    prepopulated_fields = {'slug': ('title',)}
