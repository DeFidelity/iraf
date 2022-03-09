from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User 



from wagtail.snippets.models import register_snippet
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtailmetadata.models import MetadataPageMixin



class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class BlogIndexPage(Page):
    body = RichTextField(blank=True)
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('body', classname="full"),
    ]


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=100,null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('title'),
        FieldPanel('description'),

    ]
    
    @property
    def categories(self):
        return BlogPage.objects.filter(categories__pk__in=self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'



class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context



class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return str(self.content_object)



class BlogPage(MetadataPageMixin, Page):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='author')
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField(BlogCategory, blank=True)
    date = models.DateField("Post date",auto_now=True)
    changed = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,blank=True,related_name='+')

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    def get_context(self, request, *args, **kwargs):
         context = super().get_context(request, *args, **kwargs)
         context['blog_page'] = self.blog_page


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('author'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
    
    class Meta:
        ordering = ['-date']

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class Comment(models.Model):
    blog = models.ForeignKey(BlogPage,related_name='comments',on_delete=models.CASCADE)
    author = models.ForeignKey(User,related_name='+',on_delete=models.CASCADE)
    comment = models.TextField()
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True,related_name='+')
    stars = models.PositiveSmallIntegerField(null=True,blank=True)
    date = models.DateTimeField(default=timezone.now)
    
    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False 
    
    @property
    def children(self):
        return Comment.objects.filter(parent=self).all()
    
    
    def __str__(self):
        return f"by {self.author} on {self.blog}"
