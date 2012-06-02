from django.conf.urls.defaults import *
from ryoblog import settings
import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^ryoblog/', include('ryoblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$',	'ryoarticles.views.home'),
    url(r'^a/(.+)/$',		'ryoarticles.views.single', name="single-view"),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

import sys
if sys.platform == 'win32':
	urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_DIR, 'proj_static')}),
	)