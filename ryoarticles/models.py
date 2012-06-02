from django.db import models, IntegrityError, DatabaseError
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



class Article(models.Model):
	title 		= models.CharField(max_length=250)
	slug		= models.SlugField(max_length=255, unique=True)
	content 	= models.TextField()
	created		= models.DateTimeField(auto_now_add=True)
	modified	= models.DateTimeField(auto_now=True)
	author		= models.ForeignKey(User, null=True)

	@models.permalink
	def get_absolute_url(self):
		return ('ryoarticles.views.single', [self.slug])

	def save(self):
		def_slug = slugify(self.title)
		cur_int = 2

		if not self.slug or self.slug == '':
			self.slug = def_slug

		while True:
			try:
				super(Article, self).save()
			except IntegrityError:
				self.slug = '%s-%s' % (def_slug, str(cur_int))
				cur_int += 1
			except DatabaseError:
				from django.db import connection
				connection._rollback()
			else:
				break


	def __unicode__(self):
		return self.title

