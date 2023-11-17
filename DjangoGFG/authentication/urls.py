from django.contrib import admin
from django.urls import include, path
from authentication import views

urlpatterns = [
    path('', views.home, name="home"), #'' means nothing after website domain, so just 127.0.0.1:8000/
    path('signup', views.signup, name="signup"), # means 127.0.0.1:8000/signup/
    path('gamepage', views.gamepage, name="gamepage"),
    path('suclog', views.suclog, name="suclog"),
]