from django.urls import path, include
from hubapp import views



app_name = 'hubapp'

urlpatterns = [
    path('display/', views.display, name='display'),
    path('controller/', views.controller, name='controller'),
    path('whereami/', views.whereami, name='whereami'),
    path('test/', views.test, name='test'),

    
] 