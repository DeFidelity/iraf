from django.views import View
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HTTPResponse


from .models import BlogPage, BlogCategory, Comment
from .forms import CommentForm

from django.views.generic import TemplateView
from wagtail.core.models import Site


class LandingPageView(View):
    pass

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
    def get(self,request,pk):
        blog = get_object_or_404(BlogPage,pk=pk)

        context = {}
        return render(request,'blog_detail.html',context)

class BlogComment(self):
    def get(self,request,post_pk):
        comment = Comment.objects.filter(blog__pk=post_pk)

        return render(request,'blog/comments.html')

    def post(self,request,post_pk):

        comment = request.POST.get('comment')
        post = get_object_or_404(BlogPage,pk=post_pk)

        if post:
            form = CommentForm(comment)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.user = request.user
                new_comment.blog = post
                new_comment.save()

                return HTTPResponse("comment submitted")
            return HTTPResponse("form error")
        return HTTPResponse("post not exist")

class Search(View):
    def get(self,request):
        return render(request,'blog/search.html')

    def post(self,request,*args,**kwargs):
        query = request.POST.get('query')
         report = BlogPage.objects.filter(Q)













class RobotsView(TemplateView):

    content_type = 'text/plain'
    template_name = 'robots.txt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = context['view'].request
        context['wagtail_site'] = Site.find_for_request(request)
        return context
