from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile, NewsLetter,Contact


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username','phone_number','address','gender','display_name','additional_mail')

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ('email',)
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','email','message')