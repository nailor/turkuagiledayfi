from django.contrib.syndication.feeds import Feed
from agileday.news.models import NewsItem

class LatestEntries(Feed):
    title = "Turku Agile Day news"
    link = "/news/"
    description = "Recent news recarding Turku Agile Day."
    author_email = 'info@turkuagileday.fi'

    def items(self):
        return NewsItem.published.order_by('-publish_date')[:10]

    def item_link(self, item):
        return '/news/%d/' % item.id

    def item_author_name(self, item):
        return item.author.get_full_name()

    def item_pubdate(self, item):
        return item.publish_date
