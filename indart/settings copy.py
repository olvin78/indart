from pathlib import Path
import os
from decouple import config
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-y#u%pnw+1o-ye#+pkx)1r@e(^4r)b*6l^%^j11nnt0n64#&yq2'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'applications.home',
    'applications.assistant',
    'channels',
    'rosetta',
    'tinymce',
    'parler',  # ✅ Django-Parler activado
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # ✅ Necesario para la internacionalización
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ASGI_APPLICATION = "indart.asgi.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

ROOT_URLCONF = 'indart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'indart.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ✅ Configuración de Internacionalización
LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

# ✅ Idiomas disponibles
LANGUAGES = [
    ('es', _('Español')),
    ('en', _('Inglés')),
]

# ✅ Rutas para archivos de traducción
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# ✅ Configuración de Django-Parler
PARLER_LANGUAGES = {
    None: (
        {'code': 'es'},
        {'code': 'en'},
    ),
    'default': {  
        'fallbacks': ['es'],  # Si no hay traducción, usa español
        'hide_untranslated': False,
    }
}

# ✅ Configuración de archivos estáticos
STATIC_URL = '/static/'
BASE_URL = 'localhost'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-xxxxxx")  # ✅ Clave API segura

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tuemail@gmail.com'
EMAIL_HOST_PASSWORD = 'tucontraseña'  # Usa una app password
