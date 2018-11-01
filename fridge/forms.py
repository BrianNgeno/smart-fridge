from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Grocery,Profile,Cart

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','grocery']

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        exclude = ['user','is_ordered','item','paid']