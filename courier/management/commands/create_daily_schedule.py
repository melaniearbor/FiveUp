from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware
from django.utils.timezone import get_current_timezone
import random
from random import shuffle
import datetime
from datetime import date
import math
from courier.models import UserSendTime
from fuauth.models import User

all_users = User.objects.all()
group_a = []
group_b = []
group_c = []

def divide_users(group_a, group_b, group_c):
  num_of_users = len(all_users)
  remainder_users = num_of_users%3
  users_divided_by_three = math.floor(num_of_users/3)
  group_a_total = int(users_divided_by_three)
  group_b_total = int(users_divided_by_three)
  group_c_total = int(users_divided_by_three) + remainder_users
  group_b_range = group_a_total + group_b_total
  group_c_range = group_b_range + group_c_total
  users_list = list(all_users)
  shuffle(users_list)
  group_a = users_list[0:group_a_total]
  group_b = users_list[group_a_total:group_b_range]
  group_c = users_list[group_b_range:group_c_range]
  return(group_a, group_b, group_c)


def create_schedule():
  """
  Creates 5 random send times
  per day, within the hours of 6AM and 7PM PST. Send times 
  are no closer together than 40 minutes and no farther apart than
  2 hours and 36 minutes.
  """
  
  today = date.today()
  day_start = make_aware(datetime.datetime(today.year, today.month, today.day,6,0,0,000000),get_current_timezone())
  schedule = []
  start_time = day_start
  for x in range(0,5):
    random_seconds = random.randint(2400, 9360)
    send_time = start_time + datetime.timedelta(seconds=random_seconds)
    schedule.append(send_time)
    start_time = send_time
  return schedule 

def record_user_send_times(group):
  """
  Creates send times specific to each active user who has chosen to receive messages. 
  Will reduce the number of send times created in create_schedule based on the 
  number of texts the user has chosen to receive.

  """
  group_schedule = create_schedule()
  shuffle(group_schedule)
  for user in group:
    if user.receiving_messages==True & user.is_active==True:
        user_schedule = group_schedule[0:int(user.how_many_messages)]
        for time in user_schedule:
          user_send_time = UserSendTime.objects.create(scheduled_time = time, user = user)



class Command(BaseCommand):
  def handle(self, *args, **options):
    group_q, group_r, group_s = divide_users(group_a, group_b, group_c)
    record_user_send_times(group_q)
    record_user_send_times(group_r)
    record_user_send_times(group_s)
