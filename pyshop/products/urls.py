from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('', include('django.contrib.auth.urls')),
    path('new', views.new),
    path('register', views.register)
]
