from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from agileday.utils import now

class NewsManager(models.Manager):
    def get_query_set(self):
        return super(NewsManager, self).get_query_set().filter(
            publish_date__lte=now
            )

class NewsItem(models.Model):
    title = models.CharField('title', max_length=500)
    slug = models.SlugField('url', unique=True)
    author = models.ForeignKey(User, editable=False)
    body = models.TextField()
    publish_date = models.DateTimeField(default=datetime.now)

    objects = models.Manager()
    published = NewsManager()

    def __unicode__(self):
        return '%s' % self.title

