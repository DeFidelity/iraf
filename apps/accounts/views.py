from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.views import View
from .models import UserProfile
from .forms import SignUpForm, LogInForm

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
