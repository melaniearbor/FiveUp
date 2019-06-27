# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuauth', '0018_auto_20170527_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='carrier',
            field=models.CharField(default=b'pixmbl.com', max_length=100, verbose_name='carrier', choices=[(b'mms.att.net', b'AT&T'), (b'vtext.com', b'Verizon'), (b'pixmbl.com', b'Virgin'), (b'messaging.sprintpcs.com', b'Sprint'), (b'tmomail.net', b'T-Mobile'), (b'mms.cricketwireless.net', b'Cricket'), (b'mymetropcs.com', b'Metro PCS'), (b'msg.fi.google.com', b'Project Fi'), (b'text.republicwireless.com', b'Republic Wireless'), (b'tmomail.net', b'US Mobile')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether the user should be treated as active.        Unselect this instead of deleting accounts.', verbose_name='active'),
            preserve_default=True,
        ),
    ]
