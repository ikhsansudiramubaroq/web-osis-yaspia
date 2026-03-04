from django.urls import path
from .views import *

app_name ="news"
urlpatterns = [
    path('', news_list, name='index'), # Path kosong ini untuk beranda
    path('detail_news/<slug:slug_news>', detail_news, name='detail_news'), 
]