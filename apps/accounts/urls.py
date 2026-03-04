from django.urls import path
from django.contrib.auth import views as auth_views

app_name ="accounts"
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'dashboard/login.html') , name='login'), # Path untuk mengarah ke login
    path('logout/', auth_views.LogoutView.as_view() , name='logout'), # Path untuk mengarah ke login
]