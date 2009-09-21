from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/(.*)', admin.site.root),
    (r'.*/$', view_page),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL,
         'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}
         ),
    )
