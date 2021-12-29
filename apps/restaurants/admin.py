from django.contrib import admin
from .models import Restaurant, FoodCategory, Food, Review

class RestaurantDisplay(admin.ModelAdmin):
    list_display = ['name','location','email','contact','review']
    

class FoodDisplay(admin.ModelAdmin):
    list_display = ['name','restaurant','price','review','purchase']
    
admin.site.register(Restaurant,RestaurantDisplay)
admin.site.register(Food,FoodDisplay)
admin.site.register(FoodCategory)
admin.site.register(Review)