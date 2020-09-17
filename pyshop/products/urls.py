from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index),
    path('', include('django.contrib.auth.urls')),
    path('new', views.new),
    path('register', views.register),
    path('upload', views.upload),
    path('videoshow/<int:id>/', views.videoWatch),
    path('user/<int:user_id>/', views.user_view),
    path('user/<int:id>/', views.user_update),

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

