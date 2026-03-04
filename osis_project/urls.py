from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Tambahkan baris ini!
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    
    path('', include('home.urls')), # Path kosong ini untuk beranda
    path('accounts/', include('accounts.urls')), # Path login ini untuk login
    path('dashboard/', include('dashboard.urls')), # Path login ini untuk login
    path('gallery/', include('gallery.urls')), # Path gallery ini untuk halaman galery
    path('news/', include('news.urls')), # Path news untuk halaman news/berita
] 
if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)