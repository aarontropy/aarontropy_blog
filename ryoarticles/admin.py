from ryoarticles.models import Article
from django.contrib import admin
from ryoblog import settings


class CommonMedia:
	js = (
		'http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js',
		'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.18/jquery-ui.min.js',

		settings.STATIC_URL + 'tiny_mce/jquery.tinymce.js',
		settings.STATIC_URL + 'js/aarontropy_admin.js',
	)
	css = {
	}

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'published', 'created', 'is_published')
	ordering = ['published']
	exclude = ('slug',)

	def is_published(self, obj):
		return obj.status == 'PUB'
	is_published.admin_order_field = 'status'
	is_published.boolean  = True
	is_published.short_description = 'Published?'
	
admin.site.register(Article, ArticleAdmin, Media=CommonMedia)

