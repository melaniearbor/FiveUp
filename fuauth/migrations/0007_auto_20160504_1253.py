# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuauth', '0006_auto_20160315_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='carrier',
            field=models.CharField(default=b'pixmbl.com', max_length=100, choices=[(b'txt.att.net', b'AT&T'), (b'vtext.com', b'Verizon'), (b'pixmbl.com', b'Virgin'), (b'messaging.sprintpcs.com', b'Sprint'), (b'tmomail.net', b'T-Mobile'), (b'sms.mycricket.com', b'Cricket'), (b'mymetropcs.com', b'Metro PCS'), (b'msg.fi.google.com', b'Project Fi')]),
            preserve_default=True,
        ),
    ]
