from django.db import models

import re

from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django import forms

from uuidfield import UUIDField

# Create your models here.

class UserManager(BaseUserManager):
  def _create_user(self, name, email, password, phone_number, carrier,
   user_timezone, is_staff, is_superuser):
    now = timezone.now()
    if not email:
      raise ValueError(_('Hey there! We need your email address.'))
    email = self.normalize_email(email)
    user = self.model(name=name, email=email, phone_number=phone_number, carrier=carrier, user_timezone=user_timezone, 
      is_staff=is_staff, is_superuser=is_superuser, last_login=now, date_joined=now)
    # user.uuid=uuid
    user.set_password(password)
    user.save(using=self._db)
    print('Look I did this user manager thing!')
    return user

  def create_user(self, name, phone_number,
    carrier, user_timezone, email=None, password=None):
    return self._create_user(name, email, password, phone_number, 
      carrier, user_timezone, False, False)

  def create_superuser(self, name, email, password, phone_number, 
    carrier, user_timezone):
    user=self._create_user(name, email, password, phone_number, carrier,
      user_timezone, True, True)
    user.is_active=True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser, PermissionsMixin):

    ATT = 'txt.att.net'
    VERIZON = 'vtext.com'
    VIRGIN = 'pixmbl.com'
    SPRINT = 'messaging.sprintpcs.com'
    TMOBILE = 'tmomail.net'
    CRICKET = 'mms.cricketwireless.net'
    METROPCS = 'mymetropcs.com'
    PROJECTFI = 'msg.fi.google.com'

    CARRIER_CHOICES = (
        (ATT, 'AT&T'),
        (VERIZON, 'Verizon'),
        (VIRGIN, 'Virgin'),
        (SPRINT, 'Sprint'),
        (TMOBILE, 'T-Mobile'),
        (CRICKET, 'Cricket'),
        (METROPCS, "Metro PCS"),
        (PROJECTFI, 'Project Fi')
    )

    HAWAII = 'HI'
    ALASKA = 'AK'
    PACIFIC = 'PC'
    MOUNTAIN = 'MT'
    CENTRAL = 'CN'
    EASTERN = 'EA'
    ATLANTIC = 'AT'
    TIME_ZONE_CHOICES = (
        (HAWAII, 'Hawaii'),
        (ALASKA, 'Alaska'),
        (PACIFIC, 'Pacific'),
        (MOUNTAIN, 'Mountain'),
        (CENTRAL, 'Central'),
        (EASTERN, 'Eastern'),
        (ATLANTIC, 'Atlantic')
    )

    name = models.CharField(
      _('your name'),
      max_length = 35,
      blank = True,
      null = True
    )

    email = models.EmailField(
      _('your email address'),
      unique = True,
      max_length = 255,
    )

    phone_number = models.CharField(
      _('your phone number'), 
      max_length=10)

   # TODO - Figure out default prompt value
    carrier = models.CharField(
      max_length=100,
      choices=CARRIER_CHOICES,
      default=VIRGIN
    )

    user_timezone = models.CharField(
      max_length=2,
      choices=TIME_ZONE_CHOICES,
      default=PACIFIC
    )

    is_staff = models.BooleanField(
      _('staff status'),
      default = False, 
      help_text =_('Designates whether the user can log into this admin\
        site'),
    )

    is_active = models.BooleanField(
      _('active'),
      default = False,
      help_text = _('Designates whether the user should be treated as active.\
        Unselect this instead of deleting accounts.')
    )

    date_joined = models.DateTimeField(
      _('date joined'), 
      default=timezone.now
    )

    receive_newsletter = models.BooleanField(default=False)

    uuid = UUIDField(
      blank=True, 
      null=True, 
      max_length=32, 
      auto=True
    )

    receiving_messages = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number', 'carrier', 'user_timezone']

    def get_full_name(self):
      return self.name

    def get_short_name(self):
      return self.name

    def email_user(self, subject, message, from_email=None):
      send_mail(subject, message, from_email, [self.email])

    # def get_absolute_url(self):
    #   from django.core.urlresolvers import reverse
    #   return (reverse('fuauth.views.success', args=[str(self.id)])



