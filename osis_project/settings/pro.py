from .base import *
from decouple import config # Pastikan ini ada kalau pakai .env

DEBUG = False
ALLOWED_HOSTS = ['*'] # Untuk testing awal di Docker, nanti ganti ke domain asli

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER' : config('DB_USER'),
        'PASSWORD' : config('DB_PASSWORD'),
        'HOST' : config('DB_HOST'),
        'PORT' : config('DB_PORT')
    }
}

# Keamanan tambahan
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Jangan lupa STATIC_ROOT kalau belum ada
STATIC_ROOT = BASE_DIR / 'staticfiles'