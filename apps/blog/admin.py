from django.contrib import admin
from .models import BlogPageTag, BlogPage, BlogPageGalleryImage




class BlogPageDisplay(admin.ModelAdmin):
    list_display = ('title','intro','tags','date')

admin.site.register(BlogPage,BlogPageDisplay)
admin.site.register(BlogPageTag)
admin.site.register(BlogPageGalleryImage)
