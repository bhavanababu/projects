from django import forms
from django.contrib.auth.models import User
from bookapp.models import Book
from django.contrib.auth.forms import UserCreationForm




class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model=User
        fields=["first_name","last_name","username","password1","password2","email"]
        widgets={

            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
        }


class Loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"
        widgets={"bookname":forms.TextInput(attrs={"class":"form-control"}),
                 "author": forms.TextInput(attrs={"class": "form-control"}),
                 "price": forms.NumberInput(attrs={"class": "form-control"}),
                 "qty": forms.NumberInput(attrs={"class": "form-control"}),
                 "publisher": forms.TextInput(attrs={"class": "form-control"}),
                 }
