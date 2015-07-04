# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuauth', '0003_auto_20141221_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='carrier',
            field=models.CharField(default='vmobl.com', max_length=2, choices=[('txt.att.net', 'AT&T'), ('vtext.com', 'Verizon'), ('vmobl.com', 'Virgin'), ('messaging.sprintpcs.com', 'Sprint'), ('tmomail.net', 'T-Mobile'), ('sms.mycricket.com', 'Cricket'), ('mymetropcs.com', 'Metro PCS')]),
            preserve_default=True,
        ),
    ]
