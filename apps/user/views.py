from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import UserProfile, NewsLetter
from .forms import NewsLetterForm, ProfileEditForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        profile = get_object_or_404(UserProfile,user=request.user)
        context = {
            'profile': profile
         }
        return render(request,'account/profile.html',context)

class ProfileEdit(LoginRequiredMixin,View):
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
                return HttpResponse('U dey mad, Na Your Papa account be that??')

class NewsletterView(View):
    def post(self,request,*args, **kwargs):
        form = NewsLetterForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return HttpResponse('Thanks for subscribing to our newsletter')
        
class EmailCheck(View):
    def post(self,request,*args, **kwargs):
        form = request.POST.get('email')
        newsletter = NewsLetter.objects.all()
        if form in newsletter:
            return HttpResponse("You're already a subscriber")
        elif form.length < 6:
            return HttpResponse('Please enter a valid email address')
        else:
            return HttpResponse('success')