from decouple import config 
from pathlib import Path
from datetime import timedelta
import pymysql
from pathlib import Path
pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
SECRET_KEY = 'django-insecure-0jxsgm3u+cqz+u)zhl_of45f#*zw%d9$z-mfoq%7mptmn6wm9*'
DEBUG = True
CORS_ALLOW_ALL_ORIGINS = True


ALLOWED_HOSTS = ['https://sistema-de-ventas-uumw.onrender.com']


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
    'corsheaders',
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ALLOW_HEADERS = [
    "authorization",
    "content-type",
]


ROOT_URLCONF = 'BACK.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['0.0.0.0/0'],  
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

# Base de datos
DATABASES = {
    
    
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('SQL_NAME', default='ventas2025'), 
        'USER': config('SQL_USER', default='root'), 
        'PASSWORD': config('SQL_PASSWORD'),
        'HOST': config('SQL_HOST', default='5.tcp.ngrok.io'),
        'PORT': config('SQL_PORT', default='29865'), 
        'ATOMIC_REQUESTS': False, 
        'AUTOCOMMIT': True, 
        'CONN_MAX_AGE': None,
    },
    
    'mongo_db': {
        'ENGINE': 'djongo',
        'NAME': 'juguetes', 
        'CLIENT': {
            'host': config('DATABASE_URL'),
        },
        'ATOMIC_REQUESTS': False, 
        'AUTOCOMMIT': True, 
        'CONN_MAX_AGE': None,
    }
    
   
}

# Validadores de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True


STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASE_ROUTERS = ['BACKVENTAS.router.ImageDBRouter']