from django.urls import path
from .views import *

app_name ="news"
urlpatterns = [
    path('', news_list, name='index'), # Path kosong ini untuk beranda
]