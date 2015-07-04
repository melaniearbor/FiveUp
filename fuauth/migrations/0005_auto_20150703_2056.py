# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuauth', '0004_auto_20150703_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='carrier',
            field=models.CharField(choices=[('txt.att.net', 'AT&T'), ('vtext.com', 'Verizon'), ('vmobl.com', 'Virgin'), ('messaging.sprintpcs.com', 'Sprint'), ('tmomail.net', 'T-Mobile'), ('sms.mycricket.com', 'Cricket'), ('mymetropcs.com', 'Metro PCS')], max_length=100, default='vmobl.com'),
            preserve_default=True,
        ),
    ]
