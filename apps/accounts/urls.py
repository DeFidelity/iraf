from django.urls import path
from apps.blog.views import UserCollection
from .views import (SignUpView,LogInView,ProfileView,
                    LogOutView,ProfileEdit,VerifyAccount)



urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('verification/',VerifyAccount.as_view(),name='verify'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile/edit',ProfileEdit.as_view(),name='profile-edit'),
    path('profile/collection/',UserCollection.as_view(),name='user-collection')
]
