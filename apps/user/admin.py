from django.contrib import admin
from .models import UserProfile, NewsLetter,Contact


class ProfileDisplay(admin.ModelAdmin):
    list_display = ('username', 'user', 'gender','display_name','phone_number')
    
class NewsLetterDisplay(admin.ModelAdmin):
    list_display = ('email','date')
    search_fields = ('email','date')
    
class ContactDisplay(admin.ModelAdmin):
    list_display = ('name','email','date')
    search_fields = ('message','name','email','date')
    
    
admin.site.register(UserProfile,ProfileDisplay)
admin.site.register(NewsLetter,NewsLetterDisplay)
admin.site.register(Contact,ContactDisplay)