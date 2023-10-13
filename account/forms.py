from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userregform(UserCreationForm):

    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"firstname","class":"form-control custom-field"}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"lastname","class":"form-control custom-field"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "email", "class": "form-control custom-field"}))
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"username","class":"form-control custom-field"}))
    password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"placeholder":"password","class":"form-control custom-field"}))
    password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"placeholder":"confirm password","class":"form-control custom-field"}))

   
    class Meta():
        model=User
        fields=['first_name','last_name','email','username','password','password2']


class lguform(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"name","class":"form-control custom-field"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"placeholder":"password","class":"form-control custom-field"}))