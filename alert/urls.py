from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import os

urlpatterns = [
    # Examples:
    # url(r'^$', 'alert.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('application.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
