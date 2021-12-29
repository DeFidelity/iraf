from django.urls import path
from .views import (BlogListView,LandingPageView,BlogDetailView,
                    BlogComment,Search,BlogLike,UserCollection)
urlpatterns = [
    path('',LandingPageView.as_view(),name='landing'),
    path('blogs/list/',BlogListView.as_view(),name='blog-list'),
    path('blog/<str:slug>/',BlogDetailView.as_view(),name='blog-detail'),
    path('blog/<int:pk>/comment/',BlogComment.as_view(),name='blog-comment'),
    path('search/',Search.as_view(),name='search'),
    path('blog/likes/<int:post_pk>',BlogLike.as_view(),name='blog-like'),
    path('blog/add/<int:post_pk>',UserCollection.as_view(),name='collection'),

]
