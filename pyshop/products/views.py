from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, ProductForm, UserForm
from .models import Product, UserProfile
from django.contrib.auth.models import User
import os



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
views = "0"
uploadeDay = "0"
username = "ramunas"


def upload(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id = current_user.id)
    if request.method == "POST":
        form = ProductForm(request.POST or None, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.videoTime = time
            instance.icon = profile.icon
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
    delete_file = profile.icon
    new = str(delete_file).replace("profileicons/", "")

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES or None, instance = profile)
        image_check = profile.icon
        if form.is_valid():
            
            form.save()
            if  image_check != "":
                if form.has_changed() and profile.icon != "":
                    filepath1 = request.FILES["icon"].name
                    filepath = request.FILES.get(profile.icon.path)
                    path = os.path.join("media\profileicons", new)
                    os.remove(path)
            return redirect('/user')
    else:
        form = UserForm(instance = profile)
    
    context = {
        "form": form,
        "profile":profile,
    }
    return render(request, 'user_update.html', context)
