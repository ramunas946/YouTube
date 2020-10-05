from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from products.models import Product , UserProfile
from .validators import validate_time
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = "__all__"

class ProductForm(forms.ModelForm):
    videoTime = forms.CharField(required=False)
    icon = forms.CharField(required=False)
    views = forms.CharField(required=False)
    uploadeDay = forms.CharField(required=False)
    image = forms.FileField()
    title = forms.CharField()
    username = forms.CharField(required=False)
    video = forms.FileField()
    account =forms.IntegerField(required=False)
    class Meta:
        model = Product
        fields = "__all__"
        
class UserForm(forms.ModelForm):
    icon = forms.ImageField(required=False)
    user = forms.IntegerField()
    class Meta:
        model = UserProfile
        fields = "__all__"