'''
Schedule messages for users who have chosen to received messages PER_WEEK
Schedule is always for the following week, first day is Monday (0)

Issues:  

currently using the default start and end times of day
currently using the django current timezone
code structured to facilitate switch to individual User attributes

The date when this module is run determines which week is scheduled.  

Care should be taken not to run in the first or last hours of a month
to avoid Daylight Savings Time issues.
'''         
  
from django.core.management.base import BaseCommand
import django.utils.timezone as djtz
from courier.models import UserSendTime
from fuauth.models import User
import datetime
import random
             
DEFAULT_TIMEZONE = djtz.get_current_timezone()            
DEFAULT_START_TIME = datetime.time(hour=9, tzinfo = DEFAULT_TIMEZONE)  
DEFAULT_END_TIME = datetime.time(hour=19, tzinfo = DEFAULT_TIMEZONE)          
            
def get_user_datetimes(start_date, msg_count, start_time, end_time, timezone):
    '''
    the result days should be somewhat spread throughout the week
    no duplicate days per random.sample
    ''' 
    
    #validate msg_count
    if msg_count > 6:
        msg_count = 5
    
    dates = [start_date]
    for i in range(6):
        start_date += datetime.timedelta(days=1)
        dates.append(start_date)
    
    dates = sorted(random.sample(dates, msg_count))
       
    times = []
       
    for d in dates:
        start_secs = 3600 * start_time.hour + 60 * start_time.minute 
        end_secs = 3600 * end_time.hour + 60 * end_time.minute
        
        #datetime.datetime(d.year, d.month, d.day),
        times.append(djtz.make_aware(d, djtz.get_current_timezone())
            + datetime.timedelta(seconds=random.randint(start_secs, end_secs)))
                   
    return times
    
                
def schedule_users():
    users = User.objects.filter(interval_type=User.PER_WEEK,
            receiving_messages=True, is_active=True)  
             
    now = datetime.datetime.now() 
    #truncate time elements
    today = datetime.datetime(now.year, now.month, now.day)
    start_date = today + datetime.timedelta(days= (7 - today.weekday()))

    #using the default times for all users
    for user in users:
        times = get_user_datetimes(start_date, int(user.how_many_messages), 
                DEFAULT_START_TIME, DEFAULT_END_TIME, DEFAULT_TIMEZONE)       
        for t in times:
            UserSendTime.objects.create(scheduled_time = t, user = user)
    ''' 
    # when the User class has fields to indicate individual start and end times
    # use the following instead. Will need to validate user times and convert timezone 
    for user in users:
        times = get_user_datetimes(start_date, int(user.how_many_messages), 
                user.start_time, user.end_time, CONVERT_ME(user.timezone))       
        for t in times:
            UserSendTime.objects.create(scheduled_time = t, user = user)
    ''' 
            

class Command(BaseCommand):
    def handle(self, *args, **options):
        schedule_users()
