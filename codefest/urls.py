from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codefest.views.home', name='home'),
    # url(r'^codefest/', include('codefest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'codefest.views.home',name='home'),
    url(r'^search/', 'codefest.views.search', name='search'),
    url(r'^submit_feedback/', 'codefest.views.submit_feedback', name='submit_feedback'),
    url(r'^add_sponsor/', 'codefest.views.add_sponsor', name='add_sponsor'),
    url(r'^get_sponsor/', 'codefest.views.get_sponsor', name='get_sponsor'),
)


urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, }),
)
