from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
import apps.blog.views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.blog.urls')),
    path('accounts/',include('apps.accounts.urls')),
    path('restaurants/',include('apps.restaurants.urls')),

    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
    path('sitemap.xml', sitemap),
    path('robots.txt', apps.blog.views.RobotsView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
