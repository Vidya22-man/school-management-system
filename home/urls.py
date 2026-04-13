from django.urls import path
from home import views

urlpatterns=[
    path('',views.login,name="index"),
    path('home',views.home,name='home'),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),





]