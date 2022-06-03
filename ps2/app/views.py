from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth import get_user
from .forms import RegisterForm
from .forms import LoginForm
from .forms import MessageForm
from .models import Message
from datetime import datetime

def index(request):
    form = MessageForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            message = form.cleaned_data['Message']
            owner = get_user(request)
            time = datetime.now()
            mes = Message(Text=message, Owner=owner, Date=time)
            mes.save()
            return redirect('/')
        else:
            form = MessageForm()
    form = MessageForm()
    return render(request, 'app/index.html', {'form': form, 'messages': Message.objects.all(), 'i': 1})

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth.login(request, user)

            return redirect('/')
        else:
            form = RegisterForm()

    return render(request, 'app/register.html', {'form': form})

def login(request):
    form = LoginForm(data=(request.POST or None))
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                form = LoginForm()
        else:
            form = LoginForm()
    return render(request, 'app/login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')