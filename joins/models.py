from django.db import models

class join(models.Model):
	email = models.EmailField(unique = True)
	timestamp = models.DateTimeField(auto_now = True, auto_now_add = False)
	update = models.DateTimeField(auto_now = False, auto_now_add = True)

	def __unicode__(self):
		return self.email
