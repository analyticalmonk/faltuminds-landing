from django.db import models

class join(models.Model):
	email = models.EmailField()
	ref_id = models.CharField(max_length = 120, default = 'PQR')
	ip_address = models.CharField(max_length =  120, default = 'ABC')
	timestamp = models.DateTimeField(auto_now = True, auto_now_add = False)
	update = models.DateTimeField(auto_now = False, auto_now_add = True)

	def __unicode__(self):
		return self.email

	class Meta():
		unique_together = ("email","ref_id",)
