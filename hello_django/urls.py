from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
