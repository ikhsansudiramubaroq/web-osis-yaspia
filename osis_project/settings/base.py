import sys,os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# penting agar django bisa baca folder apps/
sys.path.insert(0,os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = config('SECRET_KEY')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # apps
    'home',
    'news',
    'gallery',
    'accounts',
    'dashboard',
    'django_ckeditor_5',
    'imagekit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'osis_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'osis_project.wsgi.application'


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


CKEDITOR_5_CONFIGS = {
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'inlineTextDecoration'
        ],
        'toolbar': [
            'heading', '|', 
            'bold', 'italic', 'link', 'underline', 'strikethrough', '|',
            'bulletedList', 'numberedList', 'blockQuote', '|',
            'undo', 'redo'
        ],
    },
}

# static files css,js,images
STATIC_URL = 'static/' # fungsi agar browser akses static/(nama file static)/
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] #folder static di root project
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') #fungsi untuk collecstatic saat production

# media files user uploads
MEDIA_URL = '/media/' # fungsi agar browser akses media/(nama folder media/foto)/foto.jpg
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #lokasi menyimpan fotonya di local

# redirect setelah login dan logout
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'dashboard:dashboard_index'
LOGOUT_REDIRECT_URL = 'accounts:login'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
