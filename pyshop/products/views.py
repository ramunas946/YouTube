from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, ProductForm, UserForm
from .models import Product, UserProfile


def index(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        return render(request, 'index.html', {"products": products})
    else:
        return render(request, 'index.html', {"products": products})


def new(request):
    return HttpResponse("welcome")


def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(response, "register.html", {"form": form})


time = "2:30:40"
icon = "https://images.pexels.com/photos/827209/pexels-photo-827209.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
views = "0"
uploadeDay = "0"
username = "ramunas"


def upload(request):
    if request.method == "POST":
        form = ProductForm(request.POST or None, request.FILES)
        if form.is_valid():
            current_user = request.user
            instance = form.save(commit=False)
            instance.videoTime = time
            instance.icon = icon
            instance.views = views
            instance.uploadeDay = uploadeDay
            instance.username = current_user
            
            instance.account = current_user
            instance.save()

            return redirect("/")
    else:
        form = ProductForm()
    return render(request, "upload.html", {"form": form})


def videoWatch(response, id):
    obj = Product.objects.get(id=id)
    return render(response, 'videoshow.html', {"object": obj})


def user_view(response, id):
    
    obj = UserProfile.objects.get(user_id=user_id)
    return render(response, 'user.html', {"object": obj})

def user_update(request):
    obj = UserProfile.objects.get(id=id)
    if request.method == "POST":
        form = UserForm(request.POST or None, request.FILES)
    if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = 1
            instance.save()
            return redirect("/")
            
    return render(request, 'user.html', {"form": form,"object": obj })