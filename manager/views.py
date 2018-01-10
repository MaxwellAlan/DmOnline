from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import SigninForm,SignupForm
from account.models import UserInfo
# Create your views here.
def signin(request):
    if request.method == "POST":
        signin_form=SigninForm(request.POST)
        if signin_form.is_valid():
            cd=signin_form.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse("welcome you. you have been authenticated successfully")
            else:
                return HttpResponse("sorry.your username or password is not right")
        else:
            return HttpResponse("Invalid login")
    if request.method == "GET":
        signin_form=SigninForm()
        return render(request, "manager/signin.html")

def signup(request):
    if request.method =="POST":
        user_form=SignupForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            UserInfo.objects.create(user=new_user)
            # return HttpResponse("Successfully")
            return HttpResponseRedirect(reverse("manager:signin"))
        else:
            # return HttpResponse("fail")
            return HttpResponseRedirect(reverse("manager:signup"))
    else:
        user_form=SignupForm()
        # return render(request,"account/register.html",{"form":user_form})
        return render(request,"manager/signup.html")


