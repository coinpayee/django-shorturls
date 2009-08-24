from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from shorturls.models import ShortURL

def redirect( request, slug ):
	slug = slug.replace('/','');
	url = get_object_or_404( ShortURL, slug=slug )
	url.clicks += 1
	url.save()
	return HttpResponseRedirect( url.url )