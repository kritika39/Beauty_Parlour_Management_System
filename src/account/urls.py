#account/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin, name='admin'),
    path('homepage/', views.homepage, name='homepage'),
    path('owner_dashboard/', views.owner_dashboard, name='owner_dashboard'),
    path('logout/', views.logout_view, name='logout'),
 ]
