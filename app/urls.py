from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from sga.views import view_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', view_dashboard),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
