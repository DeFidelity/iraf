from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from apps.blog.models import BlogPage
from apps.blog.views import (BlogListView,LandingPageView,BlogDetailView,
                    BlogComment,Search,BlogLike,UserCollection,
                    CommentReplyView,CategoryList,CategoryDetail)

class TestUrls(SimpleTestCase):
    # def setUp(self):
    #     self.author = User.objects.create_user(
    #         username='author',
    #         email='author@mail.com',
    #         password='testpassword')
        
    #     self.blog = BlogPage.objects.create(
    #         author = self.author,
    #         intro = 'this is an intro', 
    #         body = 'this is the main blog', 
    #     )
        
        
    def test_homepage(self):
        home_url = reverse('landing')
        
        result = resolve(home_url)
        
        self.assertEqual(result.func.view_class,LandingPageView)
        self.assertTemplateUsed('blog/landing.html')
        
        
    def test_blog_list_urls(self):
        
        blogs = reverse('blog-list')
        
        result = resolve(blogs)
        
        self.assertEqual(result.func.view_class,BlogListView)
        self.assertTemplateUsed('blog/blog_list.html')
        
    def test_blog_details_urls(self):
        blog = reverse('blog-detail',args=['this-blog'])
        
        result = resolve(blog)
        
        self.assertEqual(result.func.view_class,BlogDetailView)
        self.assertTemplateUsed('blog/blog-detail.html')
        
    def test_blog_comment_url(self):
        comment = reverse('blog-comment',args=[2])
        
        result = resolve(comment)
        
        self.assertEqual(result.func.view_class,BlogComment)
        
    def test_search_url(self):
        search = reverse('search')
        
        result = resolve(search)
        
        self.assertEqual(result.func.view_class,Search)
        self.assertTemplateUsed('blog/search.html')
        
    def test_blog_like(self):
        like = reverse('blog-like', args=[3])
        
        result = resolve(like)
        
        self.assertEqual(result.func.view_class,BlogLike)
    
    def test_user_collection(self):
        collections = reverse('collection',args=[3])
        
        result = resolve(collections)
        
        self.assertEqual(result.func.view_class,UserCollection)
        
    def test_comment_reply_url(self):
        reply = reverse('comment-reply', args=[2,1])
        
        result = resolve(reply)
        
        self.assertEqual(result.func.view_class,CommentReplyView)
        
    def test_category_list_url(self):
        categories = reverse('category-list')
        
        result = resolve(categories)
        
        self.assertEqual(result.func.view_class,CategoryList)
        self.assertTemplateUsed('blog/category-list.html')
        
    def test_category_detail_url(self):
        category = reverse('category',args=['this category'])
        
        