from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render # Tambahkan ini untuk render template
from django.views.static import serve # Tambahkan import ini
from django.urls import re_path # Tambahkan import ini

# 1. Definisikan fungsi handler di sini agar simpel jadi satu
def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('', include('home.urls')), 
    path('admin-osis/', include('accounts.urls')), 
    path('dashboard/', include('dashboard.urls')), 
    path('gallery/', include('gallery.urls')), 
    path('news/', include('news.urls')), 
]
# 2. AKTIFKAN HANDLER (WAJIB DI LUAR URLPATTERNS)
handler404 = custom_404
handler500 = custom_500

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
    
# Pastikan ini di luar blok if DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

