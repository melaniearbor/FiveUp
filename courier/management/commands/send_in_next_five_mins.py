from django.core.management.base import BaseCommand
from django.utils import timezone
import random
from random import shuffle
import datetime
from datetime import date
import math
from courier.models import UserSendTime
from fuauth.models import User

def check_times():
	now = timezone.now()
	send_times = UserSendTime.objects.all()
	at_bat = []
	for i in send_times:
		if timezone.localtime(i.scheduled_time) < timezone.localtime(now) and i.sent == False:
			at_bat.append(i)
	return at_bat

class Command(BaseCommand):
    def handle(self, *args, **options):
    	check_times()