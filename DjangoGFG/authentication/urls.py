from django.contrib import admin
from django.urls import include, path
from authentication import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
]