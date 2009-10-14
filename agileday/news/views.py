from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from agileday.news.models import NewsItem

def display_item(request, itemid):
    newsitem = get_object_or_404(NewsItem, pk=itemid)
    return render_to_response(
        'news/archive.html',
        {'news': [newsitem]},
        context_instance=RequestContext(request)
        )

def archive(request):
    news = NewsItem.published.all()
    return render_to_response(
        'news/archive.html',
        {'news': news},
        context_instance=RequestContext(request)
        )
