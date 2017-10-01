# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
from django.db import models

# Create your models here.
class UserManager(models.Manager):

    def validate_registration(self, form_data):
        errors =[]

        if len(form_data["name"]) ==0:
            errors.append("Name is required.")

        
        if len(form_data["alias"]) ==0:
            errors.append("Alias is required.")

        
        if len(form_data["email"]) ==0:
            errors.append("Email name is required.")

        if len(form_data["dob"]) ==0:
            errors.append("Date of Birth is required.")

        if len(form_data["password"]) < 8:
            errors.append("Password must be atleast 8 characters ")

        if len(form_data["password"]) ==0:
            errors.append("Password is required.")

        if form_data["password"] != form_data["password_confirmation"]:
            errors.append("Password must match")

        return errors

    def create_user(self, form_data):
        hashedpw = bcrypt.hashpw(form_data["password"].encode(), bcrypt.gensalt())

        return User.objects.create(
            name= form_data["name"],
            alias= form_data["alias"],
            email= form_data["email"],
            password = hashedpw,
        )

    def validate_login(self, form_data):
        errors = []
        if len(form_data["email"]) ==0:
            errors.append("email is required.")

        if len(form_data["password"]) ==0:
            errors.append("password is required.")

        user = User.objects.filter(email = form_data["email"]).first()

        if user:

            if bcrypt.checkpw(form_data["password"].encode(), user.password.encode()):
                return {"user": user}
            
        return {"errors": errors}
    
    def current_user(self, request):
    
        return User.objects.get(id= request.session["user_id"])

    

class User(models.Model):
    name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)   
    email = models.CharField(max_length=45)   
    password = models.CharField(max_length=45)
    friended = models.ManyToManyField("self",related_name="friended_by")     
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()


    


    


        
