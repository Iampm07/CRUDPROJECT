from django.contrib import admin
from .models import UserProfile
#in this we register our models
@admin.register(UserProfile)
#we will make a model admin class

class UserProfileAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password']