from ryoarticles.models import Article
from django.contrib import admin


class CommonMedia:
	js = (
		'http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js',
		'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.18/jquery-ui.min.js',

#		'/static/elrte/js/elrte.min.js',
#		'/static/wymeditor/jquery.wymeditor.js',
#		'/static/nicEdit/nicEdit.js',
		'/static/tiny_mce/jquery.tinymce.js',
		'/static/aarontropy_admin.js',
	)
	css = {
		'all': ('/static/elrte/css/smoothness/jquery-ui-1.8.13.custom.css',),
		'all': ('/static/elrte/css/elrte.min.css',),
	}

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'created')
	exclude = ('slug',)
	
admin.site.register(Article, ArticleAdmin, Media=CommonMedia)

