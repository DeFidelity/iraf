from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, UserProfile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username','phone_number','address','gender')
