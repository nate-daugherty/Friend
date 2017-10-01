# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .models import *

# Create your views here.
def flash_errors(errors, request):
    for error in errors:
        messages.error(request, error)

def index(request):
    return render(request, "loginR/index.html")

def register(request):
    if request.method == "POST":
            #validate form data
        errors= User.objects.validate_registration(request.POST)
            #check if errors dont exist
    if not errors:
        user = User.objects.create_user(request.POST)
                #create the user
                #log in the user
        request.session["user_id"]= user.id
                #redirect to success page
        return redirect(reverse("landing"))

            #flash errors
    flash_errors(errors, request)
            #redirect main page

    return redirect(reverse("landing"))

def success(request):
    if "user_id" in request.session:
        
        user = current_user(request)

        friends = user.friended.all()
        
        other_users = User.objects.exclude(id__in=friends).exclude(id=user.id)
        
        context ={
            "user": user,
            "people": other_users,
            "friends": friends,
        }
        
        return render(request, "loginR/friends.html", context)
    return redirect(reverse("dashboard"))
    
def current_user(request):
    return User.objects.get(id= request.session["user_id"])

def login(request):
    if request.method =="POST":
        check= User.objects.validate_login(request.POST)

        if "user" in check:

            request.session["user_id"] = check["user"].id

            return redirect(reverse("dashboard"))

        flash_errors(check["errors"], request)

    return redirect(reverse("landing"))

def logout(request):
    request.session.flush()

    return redirect(reverse("landing"))


def friend(request, id):
    current_user = User.objects.current_user(request)

    other_users = User.objects.all()
    friend = User.objects.filter(id=id).first()

    context = {
        "user": current_user,
        "friend": friend,
        
    }
    return render(request, "loginR/user.html", context)

def add(request, id):
    current_user = User.objects.current_user(request)
    friend = User.objects.filter(id=id).first()

    current_user.friended.add(friend)

    return redirect(reverse('dashboard'))

def remove(request, id):
    current_user = User.objects.current_user(request)
    friend = User.objects.filter(id=id).first()

    current_user.friended.remove(friend)

    return redirect(reverse('dashboard'))




