from django.conf.urls.defaults import *
from settings import MEDIA_ROOT
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import global_views

urlpatterns = patterns('',
    # Example:
    # (r'^myapp/', include('myapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

## URL to serve static content
urlpatterns += patterns(
    '',
    (r'^static/(?P<path>.*)$',
     'django.views.static.serve', {
            'document_root': MEDIA_ROOT,
            }
     ),
)

urlpatterns += patterns(
    '',
    (r'^$', global_views.index),
)

urlpatterns += patterns(
    '',
    (r'^gmap/index/$', 'gmap.views.index'),
    (r'^gmap/search_ajax/$', 'gmap.views.search_city_ajax'),
    (r'^gmap/wikipedia_ajax/$', 'gmap.views.search_wikipedia_ajax'),
    (r'^gmap/route/$', 'gmap.views.route'),
)
