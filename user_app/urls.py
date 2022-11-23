from django.urls import path
from . import views


app_name = 'user_app'

urlpatterns = [

    path('login', views.ulogin, name='ulogin'),
    path('', views.base, name='base'),
    path('dashboard/<str:username>', views.profile, name = 'profile'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.logout, name = 'logout'),
    path('accounts/dashboard/', views.profile, name = 'profile'),
    # path('accounts/login/', views.login, name='login'),


] 