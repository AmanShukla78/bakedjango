# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'), name='home'),
    path('inner',TemplateView.as_view(template_name='inner.html'), name='inner'),
    path('portfolio',TemplateView.as_view(template_name='portfolio.html'), name='portfolio'),
    path('form',TemplateView.as_view(template_name='form.html'), name='form'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)