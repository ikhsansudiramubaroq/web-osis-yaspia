from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), # Path kosong ini untuk beranda
    path('gallery/', include('gallery.urls')), # Path kosong ini untuk beranda
    path('news/', include('news.urls')), # Path kosong ini untuk beranda
] 
if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)