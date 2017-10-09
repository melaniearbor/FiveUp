'''
Schedule messages for users who have chosen to received messages PER_MONTH

Issues:  

currently using the default start and end times of day
currently using the django current timezone
code structured to facilitate switch to individual User attributes

The date when this module is run determines which month is scheduled.  
see function: month_to_schedule

Care should be taken not to run in the first or last hours of a month
to avoid Daylight Savings Time issues.
'''         
  
from django.core.management.base import BaseCommand
import django.utils.timezone as djtz
from courier.models import UserSendTime
from fuauth.models import User
import calendar
import datetime
import random
             
DEFAULT_TIMEZONE = djtz.get_current_timezone()            
DEFAULT_START_TIME = datetime.time(hour=9, tzinfo = DEFAULT_TIMEZONE)  
DEFAULT_END_TIME = datetime.time(hour=19, tzinfo = DEFAULT_TIMEZONE)          
            
def get_user_datetimes(year, month, days_in_month, start_day, msg_count, 
                       start_time, end_time, timezone):
    '''
    Derive times to schedule user for the current/following month,
    randomly generated in the specified periods
    
    - year : int
    - month : int
    - days_in_month : int
    - start_day : int
        day of month to start (may be greater than 1)
    - msg_count : int
        Number of messages to schedule
    - start_time : datetime.time
        Earliest time of day to schedule
    - end_time : datetime.time
        Latest time of day to schedule
    - timezone : django.util.timezone
        Timezone to determine offset  
        
    return : list of datetimes                  
     
    
    the result days should be somewhat spread throughout the month
    no duplicate days per random.sample
    '''    
    times = []   
    days = sorted(random.sample(range(start_day, days_in_month + 1), msg_count))
    
    for d in days:
        start_secs = 3600 * start_time.hour + 60 * start_time.minute 
        end_secs = 3600 * end_time.hour + 60 * end_time.minute
        
        times.append(djtz.make_aware(datetime.datetime(year, month, d),
            djtz.get_current_timezone())
            + datetime.timedelta(seconds=random.randint(start_secs, end_secs)))
                   
    return times
    
    
def month_to_schedule(now):
    '''
    The date when this module is run determines which month
    is scheduled.  This could be the month before or very early in the
    current month.  Solution below is to schedule the next month
    if the current date has day >= 10 or the current month if day < 10,
    otherwise it won't schedule times.
    
    - now : datetime
    
    returns year, month, count of days in month, day to start scheduling (all ints)
    '''
    
    year = now.year
    month = now.month
    
    if now.day >= 10:
        if now.month == 12:
            year = now.year + 1
            month = 1
        else:    
            month = now.month + 1
        
    days_in_month = calendar.monthrange(year, month)[1] 
    
    #if scheduling after start of month, don't schedule before 'now'
    start_day = now.day if now.day < 10 else 1    

    return year, month, days_in_month, start_day   
            
            
def schedule_users():
    '''
    Add scheduled messages to UserSendTime for each active user receiving 
    FiveUp messages on the monthly plan.
    '''
    users = User.objects.filter(interval_type=User.PER_MONTH,
            receiving_messages=True, is_active=True)  
             
    now = datetime.datetime.now() 
    year, month, days_in_month, start_day =  month_to_schedule(now)

    #using the default times for all users
    for user in users:
        times = get_user_datetimes(year, month, days_in_month, 
                start_day, int(user.how_many_messages), 
                DEFAULT_START_TIME, DEFAULT_END_TIME, DEFAULT_TIMEZONE)       
        for t in times:
            UserSendTime.objects.create(scheduled_time = t, user = user)
    ''' 
    When the User class has fields to indicate individual start and end times
    use the following instead. Will need to validate user times and convert timezone 
    
    for user in users:
        times = get_user_datetimes(days_in_month, int(user.how_many_messages), 
                user.start_time, user.end_time, CONVERT_ME(user.timezone))       
        for t in times:
            UserSendTime.objects.create(scheduled_time = t, user = user)
    ''' 
            

class Command(BaseCommand):
    def handle(self, *args, **options):
        schedule_users()
