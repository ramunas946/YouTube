from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Product



def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {"products": products})


def new(request):
    return HttpResponse("welcome")


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "register.html", {"form": form})
