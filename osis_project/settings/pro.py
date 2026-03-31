from .base import *
from decouple import config, Csv # Pastikan ini ada kalau pakai .env

DEBUG = False   
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER' : config('DB_USER'),
        'PASSWORD' : config('DB_PASSWORD'),
        'HOST' : '127.0.0.1',
        'PORT' : config('DB_PORT')
    }
}

# Keamanan tambahan
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Jangan lupa STATIC_ROOT kalau belum ada
STATIC_ROOT = BASE_DIR / 'staticfiles'