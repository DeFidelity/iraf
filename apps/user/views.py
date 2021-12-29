from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import UserProfile
from .forms import ProfileEditForm
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
