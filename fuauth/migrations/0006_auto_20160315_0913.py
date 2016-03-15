# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuauth', '0005_auto_20150703_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='receiving_messages',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='carrier',
            field=models.CharField(default=b'vmobl.com', max_length=100, choices=[(b'txt.att.net', b'AT&T'), (b'vtext.com', b'Verizon'), (b'vmobl.com', b'Virgin'), (b'messaging.sprintpcs.com', b'Sprint'), (b'tmomail.net', b'T-Mobile'), (b'sms.mycricket.com', b'Cricket'), (b'mymetropcs.com', b'Metro PCS'), (b'msg.fi.google.com', b'Project Fi')]),
            preserve_default=True,
        ),
    ]
