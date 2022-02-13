from django.contrib import admin
from .models import BlogPageTag, BlogPage, BlogPageGalleryImage, Comment, BlogCategory




class BlogPageDisplay(admin.ModelAdmin):
    list_display = ('title','intro','tags','date')
    
class CommentDisplay(admin.ModelAdmin):
    list_display = ['author','blog','comment']

admin.site.register(BlogPage,BlogPageDisplay)
admin.site.register(BlogPageTag)
admin.site.register(BlogPageGalleryImage)
admin.site.register(BlogCategory)
admin.site.register(Comment,CommentDisplay)
