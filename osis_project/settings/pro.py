from .base import *

DEBUG = False
ALLOWED_HOSTS = ['domain-osis-kamu.com'] # Nanti diisi domain asli

# Keamanan tambahan
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True