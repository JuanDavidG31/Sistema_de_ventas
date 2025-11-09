from decouple import config # <-- NUEVA IMPORTACIÓN CORRECTA
from pathlib import Path
from datetime import timedelta
import pymysql
pymysql.install_as_MySQLdb()
# RUTA BASE DEL PROYECTO
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD
SECRET_KEY = 'django-insecure-0jxsgm3u+cqz+u)zhl_of45f#*zw%d9$z-mfoq%7mptmn6wm9*'
DEBUG = True

ALLOWED_HOSTS = []

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'drf_yasg',  
    'BACKVENTAS',
    'rest_framework',
]

# Middlewares necesarios para admin y autenticación
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BACK.urls'

# Configuración de plantillas (necesaria para el admin)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # si tienes una carpeta 'templates', pon su ruta aquí
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'BACK.wsgi.application'

# Base de datos (usa SQLite por ahora)
DATABASES = {
    
    
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('SQL_NAME', default='ventas2025'), # Usa config() para obtener el nombre de la BD si lo deseas
        'USER': config('SQL_USER', default='root'), 
        'PASSWORD': config('SQL_PASSWORD'), # Obtenemos la contraseña del .env o variable de entorno
        'HOST': config('SQL_HOST', default='5.tcp.ngrok.io'),
        'PORT': config('SQL_PORT', default='29865'), 
    },
    
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    #}
}

# Validadores de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Configuración regional
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'