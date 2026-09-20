from django.contrib import admin
from .models import QuoteRequest

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name','service','phone','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ('full_name','email','phone','service','project_location','message')
    readonly_fields = ('created_at',)
