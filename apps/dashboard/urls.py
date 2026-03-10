from django.urls import path
from .views import *

app_name ="dashboard"
urlpatterns = [
    path('', dashboard_index, name='dashboard_index'), # Path kosong ini untuk beranda
    
    # homepage
    path('manage-homepage', manage_homepage, name='manage_homepage'),
    # Hero (Hanya Edit)
    path('homepage/hero/edit/<int:id>/',edit_hero, name='edit_hero'),
    # Visi & Misi (Edit Singleton)
    path('homepage/visi-misi/edit/',edit_visi_misi, name='edit_visi'),
    path('homepage/misi/delete/<int:id>/', delete_misi, name='delete_misi'),
    # Agenda CRUD
    path('homepage/agenda/add/',add_agenda, name='add_agenda'),
    path('homepage/agenda/edit/<int:id>/',edit_agenda, name='edit_agenda'),
    path('homepage/agenda/delete/<int:id>/',delete_agenda, name='delete_agenda'),
    
    # activity
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