from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.views import View
from .models import UserProfile
from django.http import HttpResponse
from .forms import SignUpForm, LogInForm, ProfileEditForm

class SignUpView(View):
    def get(self,request):
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self,request,*args,**kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'accounts/signup.html', {'form': form})

class LogInView(View):
    def get(self, request):
        form = LogInForm()
        return render(request, 'accounts/login.html', {'form': form, 'error': error})

    def post(self,requst):
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                error = True

                return render(request, 'accounts/login.html', {'form': form, 'error': error})

class LogOutView(View):
    def get(self,request):
        return render(requst,'accounts/logout.html')

    def post(self,request,*args,**kwargs):
        logout(request)
        return redirect(reverse('users:login'))


class ProfileView(View):
    def get(self,request,*args,**kwargs):
        profile = get_object_or_404(UserProfile,user=request.user)
        context = {
            'profile': profile
         }
        return render(request,'accounts/profile.html')

class ProfileEdit(View):
    def get(self,request):
        return render(request,'profile_edit.html')

    def post(self,request,*args,**kwargs):
        submission = request.POST
        form = ProfileEditForm(submission)

        if form.is_valid():
            userprofile = get_object_or_404(UserProfile,user=request.user)
            if userprofile:
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()

                return redirect('profile')
            else:
                return HttpResponse('U dey mad, Na Your Papa account be that??')
