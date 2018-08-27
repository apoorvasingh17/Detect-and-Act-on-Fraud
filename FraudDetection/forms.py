from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm


class UserRegistrationForm(forms.Form):
    name = forms.CharField(
        required = True,
        label = 'NAME',
        max_length = 100
    )
    username = forms.CharField(
        required = True,
        label = 'USERNAME',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'EMAIL',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'PASSWORD',
        max_length = 32,
        widget = forms.PasswordInput()
    )


class UserAuthenticationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'USERNAME',
        max_length = 32
    )
    password = forms.CharField(
        required = True,
        label = 'PASSWORD',
        max_length = 32,
        widget = forms.PasswordInput()
    )


class question:
    class Meta:
        field=('question')



class CardForm(forms.Form):
    fullname=forms.CharField(max_length=250)
    cardnumber=forms.CharField(max_length=20)
    mm=forms.IntegerField()
    yy=forms.IntegerField()
    cvv=forms.IntegerField()
