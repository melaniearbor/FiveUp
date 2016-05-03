from django.core.management.base import BaseCommand
from django.utils import timezone
import email
import smtplib
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

def send_test_text(now_phone, now_carrier):
    message2 = "Hi there you little tiny sheep person. I think you're fantastic so I want to " \
    "send you a super duper long message. The longest you've ever seen. Unlimited! So long! and " \
    "so full of goodness and excitement!"
    msg_to = now_phone + '@' + now_carrier
    mail = EmailMultiAlternatives(
      subject="FiveUp",
      body=message2,
      from_email="Five Up <app44043297@heroku.com>",
      to=[msg_to],
    )
    mail.send()

class Command(BaseCommand):
  def handle(self, *args, **options):
    send_test_text('6192032488', 'vmobl.com')