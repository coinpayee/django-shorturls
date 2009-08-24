This is a simple url shortening service for Django.

Note: depending on your setup, you might need to use `yourappname.shorturls` instead of just `shorturls` wherever it appears in these instructions

# Installation

1. Put the shorturls folder in your Django project
2. Add `shorturls` to your INSTALLED_APPS setting
3. Add `shorturls.middleware.ShortURLMiddleware` to your MIDDLEWARE_CLASSES setting at the end (but before `django.middleware.cache.FetchFromCacheMiddleware` if you're using it)
4. Run `python manage.py syncdb` on the command line in your app folder

# Integration

If you want to have a model created a shorturl for each instance when it is created, add the following `save` method to the model (or add to your existing `save` method)

	def save( self, force_insert=False, force_update=False ):
		from shorturls.models import ShortURL
		shorturl, new = ShortURL.objects.get_or_create( url = self.get_absolute_url() )
		if new:
			shorturl.save()
		super( ModelName, self ).save( force_insert, force_update )
		
Additionally, if you want to make the shorturl available as a property of each model instance, add the following to the model:

	def shorturl( self ):
		try:
			from shorturls.models import ShortURL
			shorturl = ShortURL.objects.get( url = self.get_absolute_url() )
		except:
			shorturl = False
		return shorturl
