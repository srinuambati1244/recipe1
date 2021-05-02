from django.shortcuts import render
from . models import Receipe
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    return render(request,'login.html')


def register_page(request):
    return render(request,'register.html')


def save_details(request):
    User.objects.create_user(username=request.POST["username"], password=request.POST["password"],
                             email=request.POST["email"], phone_number=request.POST["phone_number"])
    return HttpResponseRedirect("/recp/register/")


def login_success_or_not(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/recp/show/")
    else:
        return HttpResponse("invalid username or password")


def items(request):
    r =Receipe.objects.order_by('-pub_date')
    return render(request,'show.html',{'receipe':r})


def detail(request, receipe_id):
    receipe=Receipe.objects.get(id=receipe_id)
    return render(request,'detail.html',{'receipe':receipe})


def create_page(request):
    return render(request,"create_page.html")


def save_receipe(request):
    Receipe.objects.create(receipe_name=request.POST["name"], ingredients=request.POST["ingredients"],
                           process=request.POST["process"], pub_date=timezone.now(), images=request.FILES["image"])
    return HttpResponseRedirect("/recp/show/")


def delete_receipe(request, receipe_id):
    Receipe.objects.get(pk=receipe_id).delete()
    return HttpResponseRedirect("/recp/show/")


def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/recp/")