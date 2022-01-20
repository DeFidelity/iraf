from django.urls import path 
from .views import ProfileView, ProfileEdit, NewsletterView, EmailCheck


urlpatterns = [
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile/edit/',ProfileEdit.as_view(),name='profile-edit'),
    path('newsletter/email/check/',EmailCheck.as_view(),name='email-check'),
    path('newsetter/subscribe/',NewsletterView.as_view(),name='newsletter')
]
