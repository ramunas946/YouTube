from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index),
    path('', include('django.contrib.auth.urls')),
    path('new', views.new),
    path('base', views.base),
    path('register', views.register),
    path('upload', views.upload),
    path('videoshow/<int:id>/', views.videoWatch),
    path('user/', views.user_view),
    path('user/update/<int:user_id>/', views.user_update), 

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

