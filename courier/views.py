from django.shortcuts import render
from fuauth.models import User
from messagebox.models import Message
from messagevault.models import CuratedMessage
import math
from random import shuffle
import random
import datetime
import email
import smtplib

# Create your views here.
all_users = User.objects.all()

group_a = []
group_b = []
group_c = []

def divide_users(group_a, group_b, group_c):
  num_of_users = len(all_users)
  remainder_users = num_of_users%3
  users_divided_by_three = math.floor(num_of_users/3)
  group_a_total = users_divided_by_three
  group_b_total = users_divided_by_three
  group_c_total = users_divided_by_three + remainder_users
  group_b_range = group_a_total + group_b_total
  group_c_range = group_b_range + group_c_total
  # print('all_users:' + str(all_users))
  users_list = list(all_users)
  # print('users_list:' + str(users_list))
  users_list = list(all_users)
  shuffle(users_list)
  group_a = users_list[0:group_a_total]
  # print(group_a)
  group_b = users_list[group_a_total:group_b_range]
  # print(group_b)
  group_c = users_list[group_b_range:group_c_range]
  # print(group_c)
  return(group_a, group_b, group_c)

group_a, group_b, group_c = divide_users(group_a, group_b, group_c)

print(group_a, group_b, group_c)

specialthing = 'crutchback'

def create_schedule():
  """
  Creates 5 random send times
  per day, within the hours of 6AM and 7PM PST. Send times 
  are no closer together than 40 minutes and no farther apart than
  2 hours and 36 minutes.
  """

  day_start = datetime.datetime(100, 1, 1, 6,00,00)
  schedule = []
  start_time = day_start
  for x in range(0,5):
    random_seconds = random.randint(2400, 9360)
    send_time = start_time + datetime.timedelta(seconds=random_seconds)
    schedule.append(send_time.time())
    start_time = send_time
    #print(schedule)
  return schedule 

group_a_schedule = create_schedule()
group_b_schedule = create_schedule()
group_c_schedule = create_schedule()


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

  return

def which_messages():
  print('which messages')
  message_options = ['messagebox', 'messagevault']
  picker = random.randint(0,1)
  print(message_options[picker])
  return message_options[picker]

def messagebox_pick(user):
  print('messagebox_pick')
  user_messages = Message.objects.filter(recipient=user)
  send_message = user_messages[random.randint(0,(len(user_messages))-1)]
  print(send_message)
  return send_message

def messagevault_pick():
  print('messagevault_pick')
  all_curated = CuratedMessage.objects.all()
  send_message = all_curated[random.randint(0,(len(all_curated))-1)]
  print(send_message)
  return send_message

def pick_message(user):

  user = user

  if check_for_unsent_user_messages(user) == True:
    print('user has unsent messages')
    message_group = which_messages()
    if message_group == 'messagebox':
      #mark message sent
      print('picking from messagebox')
      message_to_send = messagebox_pick(user)
    elif message_group == 'messagevault':
      print('picking from messagevault')
      message_to_send = messagevault_pick()
  else:
    print('user has no messages, picking from messagevault')
    message_to_send = messagevault_pick()

  return message_to_send

all_send_times = group_a_schedule + group_b_schedule + group_c_schedule
all_schedules = (group_a_schedule, group_b_schedule, group_c_schedule)
chron_send_times = sorted(all_send_times)

def find_time_owner(time, all_schedules):
  for schedule in all_schedules:
    if time in schedule:
      group_index = all_schedules.index(schedule)
    if group_index == 0:
      group =  group_a
      # print(group)
    elif group_index == 1:
      group =  group_b
      # print(group)
    elif group_index == 2:
      group =  group_c
      # print(group)
    return group


# def send_text():
#   msg = email.message_from_string('warning')
#   msg['From'] = "example@hotmail.fr"
#   msg['To'] = "example@hotmail.fr"
#   msg['Subject'] = "helOoooOo"

#   s = smtplib.SMTP("smtp.live.com",587)
#   s.ehlo()
#   s.starttls() 
#   s.ehlo()
#   s.login('example@hotmail.fr', 'pass')

# # s.sendmail(sender, recipient phone number, message)
#   s.sendmail("example@hotmail.fr", "example@hotmail.fr", msg.as_string())

#   s.quit()

def send_text(message, msg_to):
  msg = email.message_from_string(str(message))
  msg['From'] = "happy@fiveup.com"
  msg['To'] = msg_to
  msg['Subject'] = "" #can leave blank

  s = smtplib.SMTP("smtp.live.com",587)
  s.ehlo()
  s.starttls() 
  s.ehlo()
  s.login('melanie_crutchfield@hotmail.com', specialthing) # TODO set up a user with a password that correlates
  #to sending email account

# s.sendmail(sender, recipient phone number, message) 6192032488@vmobl.com
  s.sendmail("happy@fiveupapp.com", msg_to, msg.as_string())

  s.quit()


def pick_and_send(group):
  for user in group:
    message = pick_message(user)
    msg_to = user.phone_number + user.carrier  # TODO need to change carrier to give the email server data
    send_text(message, msg_to)




    



      





