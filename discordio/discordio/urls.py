from django.conf.urls import patterns, include, url
from blog.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.views',
    # Examples:
    # url(r'^$', 'discordio.views.home', name='home'),
    # url(r'^discordio/', include('discordio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'index'),
)
