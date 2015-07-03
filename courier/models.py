from django.db import models
from django.utils import timezone
from fuauth.models import User

# Create your models here.

class UserSendTime(models.Model):
    scheduled_time =  models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(User)

    sent = models.BooleanField(default=False)

    def __str__(self):
        ''' Gets a readable string of sender name and created_date
        to refer to the message by '''
        return '_'.join([
            str(self.user),
            str(self.scheduled_time)
        ])



# obj1 = UserSendTime.objects.create(scheduled_time=datetime.datetime(100, 1, 1, 6,14,00), user = melanie)