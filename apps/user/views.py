from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import UserProfile, NewsLetter
from apps.restaurants.models import Review
from .forms import NewsLetterForm, ProfileEditForm, ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        profile = get_object_or_404(UserProfile,user=request.user)
        review = Review.objects.filter(review_user=request.user)
        
        context = {
            'profile': profile,
            'review':review
         }
        return render(request,'account/profile.html',context)

class ProfileEdit(View):
    def get(self,request):
        profile = get_object_or_404(UserProfile,user=request.user)
        context = {
            'profile': profile
         }
        return render(request,'account/profile-edit.html',context)

    def post(self,request,*args,**kwargs):
        profile = get_object_or_404(UserProfile,user=request.user)
        submission = request.POST
        form = ProfileEditForm(submission,instance=request.user.profile)

        if form.is_valid():
            userprofile = get_object_or_404(UserProfile,user=request.user)
            if userprofile:
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()

                return redirect('profile')
            else:
                return HttpResponse('you can not do this, lol')

class NewsletterView(View):
    def post(self,request,*args, **kwargs):
        form = NewsLetterForm(request.POST)
        email = request.POST.get('email')
        try:
            newsletter = NewsLetter.objects.get(email=email)
            if newsletter:
                return HttpResponse('<p class="text-sm text-green-500 text-center">You are already a subscriber</p>')
        
        except NewsLetter.DoesNotExist:
            pass
        
        if form.is_valid():
            form.save()
            return HttpResponse('<p class="text-sm text-green-500 text-center">Thanks for subscribing to our newsletter</p>')
        
        else:
            return HttpResponse('<p class="text-sm text-green-500 text-center">kindly subscribe with a valid email</p>')
        
        
class ContactView(View):
    def get(self,request):
        return render(request,'contact.html')
    def post(self,request,*args, **kwargs):
        message = request.POST.get('message')
        form = ContactForm(request.POST)
        if len(message.split()) < 10:
            return HttpResponse('<p class="text-sm text-red-500 text-center">Form error,please write a descriptive message</p>')
            
        if form.is_valid():
            form.save()
            return HttpResponse('<p class="text-sm text-green-500 text-center">Thank you for reaching out to us, we will get back to you later</p>')
        else:
            return HttpResponse('<p class="text-sm text-red-500 text-center">Form error, please enter a valid email and descriptive message</p>')
            
            