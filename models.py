from django.db import models

class ShortURL( models.Model ):
	url		=	models.URLField( verify_exists=False, unique = True )
	slug	=	models.SlugField( max_length = 8, blank = True, null = True, unique = True )
	clicks	=	models.IntegerField( default = 0 )
	created	=	models.DateTimeField( auto_now_add = True )
	
	def __unicode__( self ):
		return u'%s' % self.url

	@models.permalink
	def get_absolute_url( self ):
		return u'/%s/' % self.slug
		
	def save( self, force_insert=False, force_update=False ):
		try:
			super( ShortURL, self ).save( force_insert, force_update )
			if not self.slug:
				length = 4
				from base64 import urlsafe_b64encode
				import hashlib
				hasher = hashlib.sha1()
				hasher.update( self.url )
				hashed = hasher.digest()
				encoded = urlsafe_b64encode( hashed ).replace( '=', '' )
				for	i in range( length, len( encoded ) ):
					start	=	i - length
					end		=	i
					try:
						self.slug = encoded[start:end]
						super( ShortURL, self ).save( force_insert, force_update )
						break;
					except:
						continue;
		except:
			pass
	class Meta:
		ordering = ( 'created', )