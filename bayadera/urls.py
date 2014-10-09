from django.conf.urls import patterns, include, url
from expense.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import login,logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^goods/$', start),
    url(r'^goods/(?P<page>.*)/(?P<brand_goods>.*)/$', start),
    url(r'^goods/(?P<page>.*)/$', start),
    url(r'^login/$', log_in),
    url( r'^logout/$', log_out),

    # url(r'^bayadera/', include('bayadera.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
