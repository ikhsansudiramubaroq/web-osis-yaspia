from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def test_home(request):
    return HttpResponse("<h1>Halo! Koneksi Django & Postgres Berhasil!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test_home), # Path kosong ini untuk beranda
]