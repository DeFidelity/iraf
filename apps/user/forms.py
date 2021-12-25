from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username','phone_number','address','gender','display_name','additional_mail')
