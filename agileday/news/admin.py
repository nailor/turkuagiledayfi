from django.contrib import admin
from agileday.news.models import NewsItem

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(NewsItem, NewsAdmin)
