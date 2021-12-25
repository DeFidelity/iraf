from django.contrib import admin
from .models import UserProfile 


class ProfileDisplay(admin.ModelAdmin):
    list_display = ('username', 'user', 'gender','display_name','phone_number')
    
admin.site.register(UserProfile,ProfileDisplay)