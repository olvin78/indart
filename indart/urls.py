from django.contrib import admin
from django.urls import path, include, re_path  # Incluye re_path desde django.urls
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from applications import home
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
# Configuración de las URLs principales
urlpatterns = [
    path('admin/', admin.site.urls),  # URL para la administración de Django
    #path('', include('applications.home.urls')),  # Ruta para la aplicación "home"
    #path('rosetta/', include('rosetta.urls')),  # URL para la interfaz de Rosetta
    
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls')),
    ]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('applications.home.urls')),  # Reemplaza 'yourapp' por tu aplicación real
    path('assistant/', include('applications.assistant.urls')),  # Ruta para la aplicación "assistant"
    path('tinymce/', include('tinymce.urls')),  # ✅ TinyMCE
)


# Configuración para servir archivos multimedia (solo en modo desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
