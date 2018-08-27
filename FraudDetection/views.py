from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import *
from django.contrib.auth.models import User
from django.http import *
from django.conf import settings
import json

from .models import EXPERIENCE
from django.template import loader

from FraudDetection.forms import *
from FraudDetection.models import QUESTION,ANSWER
from django.http import HttpResponse




def home(request):
    is_logged_in = request.user.is_authenticated
    if is_logged_in:
        return news_feed(request)
    else:
        return render(request, 'home.html')


def sign_in_up_view(request):
    signin_form = UserAuthenticationForm()
    singnup_form = UserRegistrationForm()
    return render(request, 'home.html', {'signin' : signin_form, 'signup':singnup_form})


def sign_in_view(request):
    form = UserAuthenticationForm(request.POST)
    if form.is_valid():
        userObj = form.cleaned_data
        username = userObj['username']
        password =  userObj['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            raise forms.ValidationError('Looks like a username with that email or password is incorrect!!')
    return render(request, template_name, {'form' : form})


def sign_up_view(request):
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        userObj = form.cleaned_data
        name = userObj['name']
        username = userObj['username']
        email =  userObj['email']
        password =  userObj['password']
        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username, email, password)
            user = authenticate(username = username, password = password)
            create_user(user, name)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            raise forms.ValidationError('Looks like a username with that email or password already exists')
    return render(request, template_name, {'form' : form})


