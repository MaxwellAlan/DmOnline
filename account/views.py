from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import RegisterForm,LoginForm
from .models import UserInfo

# Create your views here.
def register(request):
    if request.method =="POST":
        user_form=RegisterForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            UserInfo.objects.create(user=new_user)
            # return HttpResponse("Successfully")
            return HttpResponseRedirect(reverse("account:user_login"))
        else:
            # return HttpResponse("fail")
            return HttpResponseRedirect(reverse("account:user_register"))
    else:
        user_form=RegisterForm()
        return render(request,"account/register.html",{"form":user_form})
        # return render(request,"starter-template.html")

def user_login(request):
    if request.method == "POST":
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            cd=login_form.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse("welcome you. you have been authenticated successfully")
            else:
                return HttpResponse("sorry.your username or password is not right")
        else:
            return HttpResponse("Invalid login")
    if request.method == "GET":
        login_form=LoginForm()
        return render(request,"account/login.html",{"form":login_form})