from django.contrib import admin
from django.urls import path, include, re_path  # Incluye re_path desde django.urls
from django.conf import settings
from django.conf.urls.static import static

# Configuración de las URLs principales
urlpatterns = [
    path('admin/', admin.site.urls),  # URL para la administración de Django
    path('', include('applications.home.urls')),  # Ruta para la aplicación "home"
    path('rosetta/', include('rosetta.urls')),  # URL para la interfaz de Rosetta
    path('assistant/', include('applications.assistant.urls')),  # Ruta para la aplicación "assistant"
]

# Configuración para servir archivos multimedia (solo en modo desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
