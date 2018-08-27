from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import *
from django.contrib.auth.models import User
from django.http import *
from django.conf import settings
import json

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from django.template import loader

from FraudDetection.forms import *
from FraudDetection.models import *
from django.http import HttpResponse
from FraudDetection.models import Product


def home(request):
    is_logged_in = request.user.is_authenticated
    
    return render(request, 'home.html')


def sign_in_up_view(request):
    signin_form = UserAuthenticationForm()
    signup_form = UserRegistrationForm()
    return render(request, 'home.html', {'signin' : signin_form, 'signup':signup_form})


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
    return render(request, 'portal.html')


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
    return render(request, 'portal.html')



def card_fill(request):
    form = CardForm(request.POST)
    if form.is_valid():
        userObj = form.cleaned_data
        return HttpResponseRedirect('/')
        
    else:
        form=CardForm()
    return render(request, 'portal.html', {'form':form})

class IndexView(generic.ListView):
        # name of the object to be used in the index.html
    context_object_name = 'product_list'
    template_name = 'modelforms/index.html'
     
    def get_queryset(self):
        return Product.objects.all()
     
    # view for the product entry page
class ProductEntry(CreateView):
    model = Product
        # the fields mentioned below become the entry rows in the generated form
    fields = ['product_title', 'product_price', 'product_desc']
     
    # view for the product update page
class ProductUpdate(UpdateView):
    model = Product
        # the fields mentioned below become the entyr rows in the update form
    fields = ['product_title', 'product_price', 'product_desc']
     
    # view for deleting a product entry
class ProductDelete(DeleteView):
    model = Product
        # the delete button forwards to the url mentioned below.
    success_url = reverse_lazy('modelforms:index')
