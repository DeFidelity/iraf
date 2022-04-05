from django.test import TestCase, Client 
from django.urls import reverse 
from django.contrib.auth.models import User

from apps.blog.models import BlogPage, BlogCategory, Comment

class TestBlogViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        
        self.admin_user = User.objects.create_user(
            username = 'admin_user',
            email = 'admin@mail.com',
            password = 'testpassword'
        )
        
        self.reader_user = User.objects.create_user(
            username= 'reader_user',
            email = 'reader@mail.com',
            password = 'testpassword'
        )
        
        self.category = BlogCategory.objects.create(
            name = 'World',
            title = 'we discuss whats happening',
            description = 'what is happening in our world is discussed here'
        )
        
        self.blog = BlogPage.objects.create(
            author = self.admin_user,
            title = 'this title',
            intro = "short instroduction",
            body = 'all the discriptive body',
            categories = [self.category,]
        )
        
        self.comment = Comment.objects.create(
            blog = self.blog,
            autor = self.reader_user,
            comment = 'this is my comment',
        )
        
        
    def test_landing_page(self):
        landing = reverse('landing')
        
        response = self.client.get(landing)
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('blog/landing.html')
        
    def test_blog_list_views(self):
        blogs = reverse('blog-lists')
        
        response = self.client.get(blogs)
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('blog/blog_list.html')
        
    def test_blog_detail_view_with_get(self):
        blog = reverse('blog-detail',args=[self.blog.slug])
        
        response = self.client.get(blog)
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('blog/blog-detail.html')
        
    def test_blog_detail_view_with_POST_and_non_logged_in_user(self):
        blog = reverse('blog-detail',args=[self.blog.slug])
        
        response = self.client.post(blog,data={
            'comment': 'this is a comment'
        })
        
        self.assertEquals(response.status_code,302)
        
    def test_blog_detail_view_with_POST_and_with_logged_in_user(self):
        blog = reverse('blog-detail',args=[self.blog.slug])
        
        self.client.login(email='reader@mail.com', password= 'testpassword')
        response = self.client.post(blog,data={
            'comment': 'this is a comment'
        })
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('blog/blog-detail.html')
        
        
    def test_blog_comment_view_with_guest_user(self):
        
        comment = reverse('comment',args=[self.blog.pk])
        
        response = self.client.post(comment,data={
            'comment': 'this comment'
        })
        
        self.assertEquals(response.status_code,302)
        
        
    def test_blog_comment_view_with_logged_in_user(self):
        comment = reverse('comment',args=[self.blog.pk])
        
        self.client.login(email=self.reader_user.email,password = 'testpassword')
        response = self.client.post(comment,data={
            'comment': 'this comment'
        })
        
        self.assertEquals(response.status_code,200)
    
    
    def test_search_views_with_POST_method(self):
        search = reverse('search')
        
        response = self.client.post(search,data={
            'query': 'searching posts'
        })        
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('blog/search.html')
        
    def test_search_views_with_GET_method(self):
        search = reverse('search')
        
        response = self.client.get(search)
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('blog/search.html')
        
        
    def test_blog_like_view(self):
        like = reverse('blog-like', args=[self.blog.pk])
        
        self.client.login(email=self.reader_user.email,password = 'testpassword')
        response = self.client.post(like)
        
        self.assertEquals(response.status_code,200)
        
    def test_blog_like_view_for_guest_users(self):
        like = reverse('blog-like', args=[self.blog.pk])
        
        response = self.client.post(like)
        
        self.assertEquals(response.status_code,302)
        
        