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
        if "register" in request.POST:
            #name=request.POST.get('name')
            name=request.POST['username']
            plemail=request.POST['email']
            plpassword=request.POST['password']
            myuser = Player(username=name,email=plemail,password=plpassword)
            #myuser = User.objects.create_user(name,email,password)
            
            myuser.save()
            
            messages.success(request,"Your Account has been successfully created! You may login now")

        elif "login" in request.POST:
            email = request.POST['email']
            password = request.POST['password']
            try:
                user = Player.objects.get(email=email, password=password)
            except Player.DoesNotExist:
                user = None
            if user is not None:
                # User authentication successful
                messages.success(request, "You have successfully logged in!")
                return redirect('suclog')
            else:
                # Invalid login credentials
                messages.error(request, "Invalid login credentials")
    
    return render(request, 'login.html')


def suclog(request):
    return render(request, 'successlogin.html')

def gamepage(request):
    
    if request.method == "POST":
        if "delete" in request.POST:
            name=request.POST['username']
        try:
            user = Player.objects.get(username=name)
        except Player.DoesNotExist:
            user = None
        if user is not None:
            user.delete()
        else:
            messages.error(request, "Invalid login credentials")
    return render(request, 'game.html')
