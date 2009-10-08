from django.contrib.syndication.feeds import Feed
from agileday.news.models import NewsItem

class LatestEntries(Feed):
    title = "Turku Agile Day news"
    link = "/news/"
    description = "Updates on changes and additions to chicagocrime.org."

    def items(self):
        return NewsItem.objects.order_by('-publish_date')[:10]
