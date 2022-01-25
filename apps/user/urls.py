from django.urls import path 
from .views import ProfileView, ProfileEdit, NewsletterView, ContactView


urlpatterns = [
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile/edit/',ProfileEdit.as_view(),name='profile-edit'),
    path('newsetter/subscribe/',NewsletterView.as_view(),name='newsletter'),
    path('contact/us/',ContactView.as_view(),name="contact")
]
