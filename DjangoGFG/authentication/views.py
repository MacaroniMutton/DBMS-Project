from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Player

# Create your views here.

def home(request):
    return render(request, 'index.html')

def signup(request):
    
    if request.method == "POST":
        #name=request.POST.get('name')
        name=request.POST['username']
        plemail=request.POST['email']
        plpassword=request.POST['password']
        myuser = Player(username=name,email=plemail,password=plpassword)
        #myuser = User.objects.create_user(name,email,password)
        
        myuser.save()
        
        messages.success(request,"Your Account has been successfully created!")
    
    return render(request, 'login.html')
