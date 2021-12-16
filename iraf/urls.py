from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('blog.urls')),
    path('accounts/',include('apps.accounts.urls')),
    path('restaurants/',include('apps.restaurants.urls')),

    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
