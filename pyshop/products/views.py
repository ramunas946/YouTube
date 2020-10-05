from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, ProductForm, UserForm
from .models import Product, UserProfile
from django.contrib.auth.models import User




def index(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        return render(request, 'index.html', {"products": products})
    else:
        return render(request, 'index.html', {"products": products})

def base(request):
    user = request.user
    return render(request, 'base.html')


def new(request):
    return HttpResponse("welcome")


def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST or None)
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


def user_view(request):
    current_user = request.user
    form = UserProfile.objects.get(user_id = current_user.id)
    userform = User.objects.get(pk=current_user.id)
    context = {
        "form": form,
        "userform": userform,
    }
    return render(request, 'user.html', context)


def user_update(request, user_id):
    
    current_user = request.user
    profile = get_object_or_404(UserProfile, user_id = current_user)
    
    if request.method == "POST":
        form = UserForm(request.POST or None, request.FILES or None, instance = profile)
        if form.is_valid():

            form.save()

            return redirect('/user')
    else:
        form = UserForm(instance = profile)
    
    context = {
        "form": form,
        "profile":profile,
    }
    return render(request, 'user_update.html', context)