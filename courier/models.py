from django.db import models
from django.utils import timezone
from fuauth.models import User


class UserSendTime(models.Model):
    scheduled_time = models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    sent = models.BooleanField(default=False)

    def __str__(self):
        """ Gets a readable string of sender name and created_date
        to refer to the message by """
        return "_".join([str(self.user), str(self.scheduled_time)])
