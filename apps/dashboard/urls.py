from django.urls import path
from .views import *

app_name ="dashboard"
urlpatterns = [
    path('', dashboard_index, name='dashboard_index'), # Path kosong ini untuk beranda
    path('list-activity/', list_activity, name='list_activity'), # Path daftar activity
    path('list-gallery/', list_gallery, name='list_gallery'), # Path daftar gallery
]