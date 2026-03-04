from django.urls import path
from .views import *

app_name ="dashboard"
urlpatterns = [
    path('', dashboard_index, name='dashboard_index'), # Path kosong ini untuk beranda
]