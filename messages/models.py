from django.db import models

# Create your models here.

class Message(models.Model):

	# def get_user_id:
	# 	# put something here to get the uuid of the person
	# 	# who sent the referral link
	# 	# TODO - set AUTH_USER_MODEL to custom user model
	# 	user_id = self.kwargs[‘uuid’]
	# 	return user_id

	# recipient = self.get_user_id()
	recipient = models.CharField(
		max_length=32)
	sender_name = models.CharField(
		max_length = 35
	)
	message_text = models.TextField(
		max_length=125
	)
	created_date = models.DateTimeField(auto_now=True)
	message_sent_to = models.CommaSeparatedIntegerField(
		max_length=None
	)

	def __str__(self):
		''' Gets a readable string of sender name and created_date
		to refer to the message by '''
		return '_'.join([
			self.sender_name,
			str(self.created_date)
		])

	def get_absolute_url(self):
		''' returns a reference for the message in detail
		view.'''
		# TODO Create message detail view
		return reverse('message-detail-view', kwargs={'pk': self.id})



