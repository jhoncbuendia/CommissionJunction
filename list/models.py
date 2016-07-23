from django.db import models

class ListModel(models.Model):
	name = models.CharField(max_length = 100)
	productos = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name = "lista"
		verbose_name_plural = "listas"

	def __unicode__(self):
		return self.name
	#end def