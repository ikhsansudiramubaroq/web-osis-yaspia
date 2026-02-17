from django.urls import path
from .views import *

app_name ="gallery"
urlpatterns = [
    path('', gallery_list, name='index'), # Path kosong ini untuk beranda
]