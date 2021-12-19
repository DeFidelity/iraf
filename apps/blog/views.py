from django.views import View
from django.shortcuts import render
from django.core.paginator import Paginator


from .models import BlogPage, BlogCategory


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














class RobotsView(TemplateView):

    content_type = 'text/plain'
    template_name = 'robots.txt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = context['view'].request
        context['wagtail_site'] = Site.find_for_request(request)
        return context
