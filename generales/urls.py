from django.urls import path

from generales import views 

# Vistas para Login y Logout
from django.contrib.auth import views as auth_views

from generales.views import Home 

urlpatterns = [
    # path('', views.home, name='home'),
    
    path('',Home.as_view(), name='home'),
    
    #Login y Logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
     
]
