from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

class NewsItem(models.Model):
    title = models.CharField('title', max_length=500)
    slug = models.SlugField('url', unique=True)
    author = models.ForeignKey(User, editable=False)
    body = models.TextField()
    publish_date = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.publish_date)
