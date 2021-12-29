from django.views import View
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import BlogPage, BlogCategory, Comment
from .forms import CommentForm

from wagtail.core.models import Site


class LandingPageView(View):
    def get(self,request):
        return render(request,'blog/landing.html')

class BlogListView(View):
    def get(self,request):
        blogs = BlogPage.objects.all()
        paginator = Paginator(blogs, 15)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context= {
            'page_obj': page_obj,
            'blogs': blogs,
        }
        return render(request,'blog/blog_list.html',context)

class BlogDetailView(View):
    def get(self,request,slug):
        blog = get_object_or_404(BlogPage,slug=slug)

        context = {
            'blog':blog
        }
        return render(request,'blog/blog-detail.html',context)

class BlogComment(LoginRequiredMixin,View):
    def get(self,request,pk):
        comment = Comment.objects.filter(post=pk)

        return render(request,'blog/comments.html')

    def post(self,request,pk):

        comment = request.POST.get('comment')
        post = get_object_or_404(BlogPage,pk=pk)

        if post:
            form = CommentForm(comment)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.user = request.user
                new_comment.blog = post
                new_comment.save()

                return HttpResponse("comment submitted")
            return HttpResponse("form error")
        return HttpResponse("post not exist")

class Search(View):
    def get(self,request):
        return render(request,'blog/search.html')

    def post(self,request,*args,**kwargs):
        blog = BlogPage.objects.all()
        query = request.POST.get('query')

        report = blog.filter(
            Q(title__icontains=query) |
            Q(intro__icontains=query) |
            Q(body__icontains=query)
        )

        context = {
            'blog': blog,
            'reports': report,
        }
        print(query)
        print(report)
        return render(request,'blog/search.html',context)

class BlogLike(LoginRequiredMixin,View):
    def post(self,request,post_pk):
        blog = get_object_or_404(BlogPage,pk=post_pk)
        liked_users = blog.likes.all()
        user = request.user
        
        if len(liked_users) > 0:
            for person in liked_users:
                print(person)
                if user == person:
                    print(2)
                    blog.likes.remove(user)

                    return HttpResponse('-1')
                else:
                    print(1)
                    blog.likes.add(request.user)
                    return HttpResponse('+1')
        else:
            blog.likes.add(request.user)
        return HttpResponse('+1')


class UserCollection(LoginRequiredMixin,View):
    def post(self,request,post_pk,*args,**kwargs):
        post = get_object_or_404(BlogPage,pk=post_pk)
        user =request.user
        profile = user.profile.collections.all()
        
        if post not in profile:
            user.profile.collections.add(post)
            user.save()

            return HttpResponse('Added to collection')
        else:
            user.profile.collections.remove(post)
            user.save()
            return HttpResponse('removed from collection')
        












class RobotsView(TemplateView):

    content_type = 'text/plain'
    template_name = 'robots.txt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = context['view'].request
        context['wagtail_site'] = Site.find_for_request(request)
        return context
