from django.db import models, IntegrityError, DatabaseError
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime



class Article(models.Model):
	STATUS_CHOICES = (
		('PUB', 'Published'),
		('UPUB', 'Unpublished'),
	)

	title 		= models.CharField(max_length=250)
	slug		= models.SlugField(max_length=255, unique=True)
	status		= models.CharField(max_length=10, choices=STATUS_CHOICES, default='PUB')
	content 	= models.TextField()
	published	= models.DateTimeField(default=None, blank=True, null=True)
	created		= models.DateTimeField(auto_now_add=True)
	modified	= models.DateTimeField(auto_now=True)
	author		= models.ForeignKey(User, null=True)

	@models.permalink
	def get_absolute_url(self):
		return ('ryoarticles.views.single', [self.slug])

	def save(self):
		def_slug = slugify(self.title)
		cur_int = 2

		#
		# Publishing this for the first time, add publish date
		# (notice that the super.save() routine is called when we work on the slug below)
		if self.status == 'PUB' and self.published is None :
			self.published = datetime.now()

		#
		# Save the slug and make sure that it is unique
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

		


	def is_published(self):
		return self.status == 'PUB'
	is_published.boolean  = True
	is_published.short_description = 'Published?'

	def __unicode__(self):
		return self.title

