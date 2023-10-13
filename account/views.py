from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,FormView,CreateView,ListView
from django.contrib.auth import authenticate,login,logout
from .forms import lguform,userregform
from django.urls import reverse_lazy
from .models import Doctordeatails
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
class home(TemplateView):
    template_name="index.html"
    
class lguview(FormView):
    template_name="Log.html"
    form_class=lguform
    def post(self,request,*args,**kwargs):
        form_data=lguform(data=request.POST)
        if form_data.is_valid():
            user=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user_ob=authenticate(request,username=user,password=pswd)
            if user_ob:
                  login(request,user_ob)
                  messages.success(request,'login success')
                  return redirect('home')
            else:
                 messages.error(request,'invalid username or password')
                 return render(request,'Log.html',{"form":form_data})

class userregview(CreateView):
    template_name="reg.html"
    form_class=userregform
    success_url=reverse_lazy("log")


class doctorview(ListView):
    template_name="doctordeatails.html"
    model=Doctordeatails
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Doctordeatails.objects.all()
        return context
    
class Appoimentview(TemplateView):
    template_name="bookdoctor.html"
    
class paymentview(TemplateView):
    template_name='payment.html'
    



    
 
    
    

    
 