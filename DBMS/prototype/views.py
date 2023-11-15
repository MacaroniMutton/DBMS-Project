from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render (request, "prototype/index.html")

def signup(request):
    return render (request, "prototype/signup.html") #render a html template for signup made in prototype app directory when request is asked and return that render

def signin(request):
    return render (request, "prototype/signin.html")

def signout(request):
    pass #since we dont want to render any template for signout, we just pass