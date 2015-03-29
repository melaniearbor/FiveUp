from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class CuratedMessage(models.Model):

	message_text = models.TextField(
		max_length=125
	)
	message_author_first = models.CharField(
		max_length=35)

	message_author_last = models.CharField(
		max_length=35)

	def __str__(self):
		''' Gets a readable string of author last name and first 45
		characters of the message  '''
		return '-'.join([
			self.message_author_last,
			self.message_text[0:45]
		])



