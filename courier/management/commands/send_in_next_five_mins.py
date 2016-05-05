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
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

def check_times():
    now = timezone.now()
    send_times = UserSendTime.objects.all()
    at_bat = []
    for i in send_times:
        if timezone.localtime(i.scheduled_time) < timezone.localtime(now) and not i.sent 
        and i.user.receiving_messages:
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

    recipient = user
    if len(Message.objects.filter(recipient=recipient, message_sent=False))==0:
        return False
    else:
        return True

def which_messages():
    picker = random.randint(0,10)
    if picker < 8:
        category = 'messagevault'
    else:
        category = 'messagebox'
    return category

def messagebox_pick(user):
    unsent_user_messages = Message.objects.filter(recipient=user, message_sent=False)
    chosen_message = unsent_user_messages[random.randint(0,(len(unsent_user_messages))-1)]
    send_message = chosen_message.message_text + ' -' + chosen_message.sender_name
    return send_message, chosen_message

def messagevault_pick():
    print('messagevault_pick')
    all_curated = CuratedMessage.objects.all()
    chosen_message = all_curated[random.randint(0,(len(all_curated))-1)]
    send_message = chosen_message.message_text + ' -' + chosen_message.message_author_first + " " + chosen_message.message_author_last
    return send_message, chosen_message

def pick_message(user):

    user = user

    if check_for_unsent_user_messages(user) == True:
        message_group = which_messages()
        if message_group == 'messagebox':
            message_to_send, chosen_message = messagebox_pick(user)
            chosen_message.message_sent = True
            chosen_message.save()
        elif message_group == 'messagevault':
            message_to_send, chosen_message = messagevault_pick()
    else:
        message_to_send, chosen_message = messagevault_pick()

    return message_to_send

def send_text(message, msg_to):


    sg = sendgrid.SendGridClient('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')

    message = sendgrid.Mail()
    message.add_to('msg_to')
    message.set_subject('')
    message.set_html('')
    message.set_text('message')
    message.set_from('Five Up <app44043297@heroku.com>')
    status, msg = sg.send(message)



def send_each_at_bat():
    at_bat = check_times()
    for i in at_bat:
        message = pick_message(i.user)
        msg_to = i.user.phone_number + '@' + i.user.carrier
        mail = EmailMultiAlternatives(
          subject="FiveUp",
          body=message,
          from_email="Five Up <app44043297@heroku.com>",
          to=[msg_to],
        )
        mail.send()
        i.sent = True
        i.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_each_at_bat()
