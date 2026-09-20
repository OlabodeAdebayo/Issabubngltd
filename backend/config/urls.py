from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from django.views.decorators.http import require_GET

@require_GET
def api_root(request):
    return JsonResponse({
        'name':'ISSABUB Nigeria Limited API',
        'version':'1.0',
        'status':'ok',
        'endpoints':['/api/company/','/api/services/','/api/projects/','/api/quotes/','/api/health/']
    })

@require_GET
def health(request):
    return JsonResponse({'status':'ok','service':'issabub-api'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),
    path('api/health/', health),
    path('api/company/', include('company.urls')),
    path('api/services/', include('services.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/quotes/', include('quotes.urls')),
]
