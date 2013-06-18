from django.conf.urls import patterns, include, url
from eater.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('eater.views',
    # Examples:
    # url(r'^$', 'twiteat.views.home', name='home'),
    # url(r'^twiteat/', include('twiteat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main'),
)
