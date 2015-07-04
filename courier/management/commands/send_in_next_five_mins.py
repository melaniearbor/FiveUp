from django.core.management.base import BaseCommand
from django.utils import timezone
import random
from random import shuffle
import datetime
from datetime import date
import math
import email
import smtplib
from courier.models import UserSendTime
from fuauth.models import User
from messagevault.models import CuratedMessage
from messagebox.models import Message

def check_times():
	now = timezone.now()
	send_times = UserSendTime.objects.all()
	at_bat = []
	for i in send_times:
		if timezone.localtime(i.scheduled_time) < timezone.localtime(now) and i.sent == False:
			at_bat.append(i)
	return at_bat

def check_for_unsent_user_messages(user):
	"""
	Checks if a user has unsent message in messagebox

		Args: 
		user: a user from fuauth

		Returns:
		False if user has no messages 
		True if user has messages 
	"""

	uuid = user.uuid
	if Message.objects.filter(recipient__uuid=uuid, message_sent=False)==[]:
		return False
	else:
		return True

def which_messages():
	# print('which messages')
	message_options = ['messagebox', 'messagevault']
	picker = random.randint(0,1)
	# print(message_options[picker])
	return message_options[picker]

def messagebox_pick(user):
	# print('messagebox_pick')
	user_messages = Message.objects.filter(recipient=user)
	chosen_message = user_messages[random.randint(0,(len(user_messages))-1)]
	send_message = chosen_message.message_text + ' -' + chosen_message.sender_name
	# print(send_message)
	return send_message

def messagevault_pick():
	print('messagevault_pick')
	all_curated = CuratedMessage.objects.all()
	chosen_message = all_curated[random.randint(0,(len(all_curated))-1)]
	send_message = chosen_message.message_text + ' -' + chosen_message.message_author_first + " " + chosen_message.message_author_last
	print(send_message)
	return send_message

def pick_message(user):

	user = user

	if check_for_unsent_user_messages(user) == True:
		# print('user has unsent messages')
		message_group = which_messages()
	if message_group == 'messagebox':
		#TODO mark message as sent
		# print('picking from messagebox')
		message_to_send = messagebox_pick(user)
		message_to_send.message_sent = True
		message_to_send.save()
	elif message_group == 'messagevault':
		# print('picking from messagevault')
		message_to_send = messagevault_pick()
	else:
		# print('user has no messages, picking from messagevault')
		message_to_send = messagevault_pick()

	return message_to_send

def send_text(message, msg_to):
	msg = email.message_from_string(str(message))
	msg['From'] = "melanie_crutchfield@hotmail.com"
	msg['To'] = msg_to
	msg['Subject'] = "" #can leave blank

	s = smtplib.SMTP("smtp.live.com",587)
	s.ehlo()
	s.starttls() 
	s.ehlo()
	s.login('melanie_crutchfield@hotmail.com', 'crutchback') # TODO set up a user with a password that correlates
	#to sending email account

	# s.sendmail(sender, recipient phone number, message) 6192032488@vmobl.com
	s.sendmail("melanie_crutchfield@hotmail.com", msg_to, msg.as_string())

	s.quit()


def send_each_at_bat():
	at_bat = check_times()
	for i in at_bat:
		message = pick_message(i.user)
		msg_to = i.user.phone_number + '@' + i.user.carrier  # TODO need to change carrier to give the email server data
		send_text(message, msg_to)


class Command(BaseCommand):
    def handle(self, *args, **options):
    	check_times()