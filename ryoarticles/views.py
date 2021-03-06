from ryoarticles.models import Article
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext


def home(request):
	articles = Article.objects.filter(status__exact='PUB').order_by('-published')[:10]
	return render_to_response('ryoarticles/mainlist.html',
		{'articles': articles},
		context_instance=RequestContext(request))

def single(request, slug):
	article = get_object_or_404(Article, slug=slug)
	return render_to_response('ryoarticles/single.html',
		{'article': article},
		context_instance=RequestContext(request))
	
