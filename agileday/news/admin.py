from django.contrib import admin
from django.conf import settings
from agileday.news.models import NewsItem

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

    class Media:
        js = (
            '%s/tinymce/jscripts/tiny_mce/tiny_mce_popup.js' % settings.MEDIA_URL,
            '%s/tinymce/jscripts/tiny_mce/tiny_mce.js' % settings.MEDIA_URL,
            '%s/filebrowser/js/TinyMCEAdmin.js' % settings.MEDIA_URL,
            )

admin.site.register(NewsItem, NewsAdmin)
