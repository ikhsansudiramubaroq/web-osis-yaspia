from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import messages

# Kita buat class kecil untuk "menyisipkan" pesan logout
class MyLogoutView(auth_views.LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            messages.success(request, "Anda telah berhasil keluar. Sampai jumpa lagi!")
        return super().dispatch(request, *args, **kwargs)
    
app_name ="accounts"
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'dashboard/login.html',redirect_authenticated_user=True) , name='login'), # Path untuk mengarah ke login
    path('logout/', MyLogoutView.as_view(next_page='accounts:login') , name='logout'), # Path untuk mengarah ke login
]