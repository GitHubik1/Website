from django.contrib.auth.forms import UserCreationForm
import django.contrib.auth.forms as aforms 
from django.contrib.auth.models import User
from django import forms
from .models import Message

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(aforms.AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']

class MessageForm(forms.Form):
    Message = forms.CharField(max_length=255)