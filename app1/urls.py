from django.urls import path
from . import views
from app1.views import login,logout,register_view

urlpatterns = [

    path('',views.index, name="index"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register/', views.register_view, name='register'),
    path('stake_create/',views.stake_create, name='stake_create'),

]
