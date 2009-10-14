from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from agileday.feeds import LatestEntries

feeds = {
    'news': LatestEntries,
    }

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^admin/(.*)', admin.site.root),
    (r'^news/$', 'agileday.news.views.archive'),
    (r'^news/([0-9]+)/$', 'agileday.news.views.display_item'),
    (r'^feeds/(?P<url>.*)/$',
     'django.contrib.syndication.views.feed',
     {'feed_dict': feeds}),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/media/favicon.ico'}),
    (r'', 'agileday.riskicms.views.view_page'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL,
         'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}
         ),
    )
