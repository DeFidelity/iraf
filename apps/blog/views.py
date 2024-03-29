from django.views import View
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.restaurants.models import Food, Restaurant
from apps.user.newslettermail import send_weekly_mail

from .models import BlogPage, BlogCategory, Comment
from .forms import CommentForm

from wagtail.core.models import Site


class LandingPageView(View):
    def get(self,request):
        send_weekly_mail()
        return render(request,'blog/landing.html')

class BlogListView(View):
    def get(self,request):
        blogs = BlogPage.objects.all()
        categories = BlogCategory.objects.all()[:4]
        paginator = Paginator(blogs, 15)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context= {
            'page_obj': page_obj,
            'categories': categories,
            'blogs': blogs,
        }
        return render(request,'blog/blog_list.html',context)

class BlogDetailView(View):
    def get(self,request,slug):
        blog = get_object_or_404(BlogPage,slug=slug)
        comments = Comment.objects.filter(blog=blog,parent=None)
        blogs = BlogPage.objects.all().exclude(slug=slug).order_by('likes')
        relative_posts = BlogPage.objects.filter(categories__pk__in=blog.categories.all()).exclude(slug=slug)[:3]
        
        context = {
            'blog':blog,
            'comments':comments,
            'blogs': blogs,
            'category': relative_posts,
        }
        return render(request,'blog/blog-detail.html',context)
    
    @method_decorator(login_required())
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

class BlogComment(View):
    @method_decorator(login_required())
    def post(self,request,pk):
        post = get_object_or_404(BlogPage,pk=pk)

        if post:
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.author = request.user
                new_comment.blog = post
                new_comment.save()

                return HttpResponse("comment submitted")
            return HttpResponse("form error")
        return HttpResponse("post not exist")

class Search(View):
    def get(self,request):
        return render(request,'blog/search.html')

    def post(self,request,slug=None,*args,**kwargs):
        blog = BlogPage.objects.all()
        query = request.POST.get('query')

        blog_result = blog.filter(
            Q(title__icontains=query) |
            Q(intro__icontains=query) |
            Q(body__icontains=query)
        )

        food = Food.objects.all()
        food_result = food.filter(Q(name__icontains=query)| Q(description__icontains=query))
        
        restaurant = Restaurant.objects.all()
        restaurant_result = restaurant.filter(Q(name__icontains=query)| Q(description__icontains=query))
        
        context = {
            'blog': blog,
            'blog_result': blog_result,
            'food_result':food_result,
            'restaurant_result': restaurant_result,
        }
        return render(request,'blog/search.html',context)

class BlogLike(View):
    @method_decorator(login_required())
    def post(self,request,post_pk):
        blog = get_object_or_404(BlogPage,pk=post_pk)
        liked_users = blog.likes.all()
        user = request.user
        
        if len(liked_users) > 0:
            # for person in liked_users:
            if request.user in liked_users:
                blog.likes.remove(user)
                return HttpResponse('-1')
            else:
                blog.likes.add(request.user)
                return HttpResponse('+1')


class UserCollection(View):
    @method_decorator(login_required())
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
        

class CommentReplyView(View):
    def get(self,request,pk,c_pk,*args,**kwargs):
        parent = get_object_or_404(Comment,pk=c_pk,blog=pk)
        blog = get_object_or_404(BlogPage,pk=pk)
        replies = Comment.objects.filter(parent=parent)
        
        context = {
            'replies':replies,
            'comment':parent,
            'blog':blog
        }
        
        return render(request,'blog/partials/reply.html',context)
    
    @method_decorator(login_required())
    def post(self,request,pk,c_pk,*args,**kwargs):
        parent = get_object_or_404(Comment,pk=c_pk)
        post = get_object_or_404(BlogPage,pk=pk)
        replies = Comment.objects.filter(parent=parent)
        if post:
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.author = request.user
                new_comment.parent = parent
                new_comment.blog = post
                new_comment.save()
                
                context = {
                    'blog':post,
                    'comment':parent,
                    'replies': replies,
                    }
                "'messages.success(request,'reply added')'"
                return render(request,'blog/partials/replies.html',context)
            return HttpResponse("form error")
        return HttpResponse("post not exist")

class CategoryDetail(View):
    def get(self,request,category,*args,**kwargs):
        category = get_object_or_404(BlogCategory,name=category)
        # category_blogs = BlogPage.objects.filter(categories__id__in=category)
        category_blogs = BlogPage.objects.filter(categories__name=category)
        print(category_blogs)
        
        context = {
            'category':category,
            'blogs': category_blogs
        }
        return render(request,'blog/category.html',context)
        
class CategoryList(View):
    def get(self,request):
        categories = BlogCategory.objects.all()
        context = {
            'categories':categories,
        }
        return render(request,'blog/category-list.html',context)
    







class RobotsView(TemplateView):

    content_type = 'text/plain'
    template_name = 'robots.txt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = context['view'].request
        context['wagtail_site'] = Site.find_for_request(request)
        return context
