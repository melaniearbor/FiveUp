from django.core.management.base import BaseCommand
from courier.models import UserSendTime

def clear_old_send_times():
	send_times = UserSendTime.objects.all()

	for i in range(2000,len(send_times)):
		send_times[i].delete()

class Command(BaseCommand):
	def handle(self, *args, **options):
	    clear_old_send_times()