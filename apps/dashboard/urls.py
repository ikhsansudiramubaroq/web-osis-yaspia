from django.urls import path
from .views import *

app_name ="dashboard"
urlpatterns = [
    path('', dashboard_index, name='dashboard_index'), # Path kosong ini untuk beranda
    path('list-activity/', list_activity, name='list_activity'), # Path daftar activity
    path('add-activity/', add_activity, name='add_activity'), # Path tambah activity
    path('update-activity/<slug:slug>/', edit_activity, name='edit_activity'), # Path edit activity
    path('activity/delete/<slug:slug>/', delete_activity, name='delete_activity'), # delete activity
    
    # gallery
    path('list-gallery/', list_gallery, name='list_gallery'), # Path daftar gallery
    path('add-gallery/', add_gallery, name='add_gallery'), # Path daftar gallery
    path('update-gallery/<int:id>/', edit_gallery, name='edit_gallery'), # Path edit gallery
    path('gallery/delete/<int:id>/', delete_gallery, name='delete_gallery'), #delete galery
]