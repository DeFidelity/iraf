from django.urls import path 
from .views import ProfileView, ProfileEdit
urlpatterns = [
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile/edit/',ProfileEdit.as_view(),name='profile-edit'),
]
