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
# import sendgrid
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

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
    return send_message, chosen_message

def messagevault_pick():
    print('messagevault_pick')
    all_curated = CuratedMessage.objects.all()
    chosen_message = all_curated[random.randint(0,(len(all_curated))-1)]
    send_message = chosen_message.message_text + ' -' + chosen_message.message_author_first + " " + chosen_message.message_author_last
    print(send_message)
    return send_message, chosen_message

def pick_message(user):

    user = user

    if check_for_unsent_user_messages(user) == True:
        # print('user has unsent messages')
        message_group = which_messages()
    if message_group == 'messagebox':
        #TODO mark message as sent
        # print('picking from messagebox')
        message_to_send, chosen_message = messagebox_pick(user)
        chosen_message.message_sent = True
        chosen_message.save()
    elif message_group == 'messagevault':
        # print('picking from messagevault')
        message_to_send, chosen_message = messagevault_pick()
    else:
        # print('user has no messages, picking from messagevault')
        message_to_send, chosen_message = messagevault_pick()

    return message_to_send

def send_text(message, msg_to):
    # msg = email.message_from_string(str(message))
    # msg['From'] = "melanie_crutchfield@hotmail.com"
    # msg['To'] = msg_to
    # msg['Subject'] = "" #can leave blank

    # s = smtplib.SMTP("smtp.live.com",587)
    # s.ehlo()
    # s.starttls() 
    # s.ehlo()
    # s.login()
    # #to sending email account

    # # s.sendmail(sender, recipient phone number, message) 6192032488@vmobl.com
    # s.sendmail("melanie_crutchfield@hotmail.com", msg_to, msg.as_string())

    # s.quit()


    sg = sendgrid.SendGridClient('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')

    message = sendgrid.Mail()
    message.add_to('msg_to')
    message.set_subject('')
    message.set_html('')
    message.set_text('message')
    message.set_from('Five Up <app44043297@heroku.com>')
    status, msg = sg.send(message)


# API Key SendGrid: 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

def send_each_at_bat():
    at_bat = check_times()
    for i in at_bat:
        message = pick_message(i.user)
        msg_to = i.user.phone_number + '@' + i.user.carrier  # TODO need to change carrier to give the email server data
        # send_text(message, msg_to)
        mail = EmailMultiAlternatives(
          subject="FiveUp",
          body=message,
          from_email="Five Up <app44043297@heroku.com>",
          to=[msg_to],
          # headers={"Reply-To": "support@sendgrid.com"}
        )
        mail.send()
        i.sent = True
        i.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_each_at_bat()
