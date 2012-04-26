from django.conf.urls.defaults import patterns, include, url
from backend.api import WineResource

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

wine_resource = WineResource()

urlpatterns = patterns('',
    (r'^api/', include(wine_resource.urls)),
    (r'^$', 'backbone_tutorial.frontend.views.index')
    # Examples:
    # url(r'^$', 'backbone_tutorial.views.home', name='home'),
    # url(r'^backbone_tutorial/', include('backbone_tutorial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
