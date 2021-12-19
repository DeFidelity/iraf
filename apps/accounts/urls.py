from django.urls import path
from .views import SignUpView,LogInView,ProfileView,LogOutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/',ProfileView.as_view(),name='profile')
]
