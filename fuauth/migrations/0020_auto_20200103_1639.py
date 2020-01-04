# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuauth', '0019_auto_20181212_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='carrier',
            field=models.CharField(verbose_name='carrier', max_length=100, default='pixmbl.com', choices=[('mms.att.net', 'AT&T'), ('vtext.com', 'Verizon'), ('pixmbl.com', 'Virgin'), ('messaging.sprintpcs.com', 'Sprint'), ('tmomail.net', 'T-Mobile'), ('mms.cricketwireless.net', 'Cricket'), ('mymetropcs.com', 'Metro PCS'), ('msg.fi.google.com', 'Project Fi'), ('text.republicwireless.com', 'Republic Wireless'), ('tmomail.net', 'US Mobile')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='user',
            name='how_many_messages',
            field=models.CharField(max_length=1, default=5, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(verbose_name='last login', blank=True, null=True),
        ),
    ]
