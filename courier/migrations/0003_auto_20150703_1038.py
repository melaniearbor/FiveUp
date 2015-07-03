# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0002_usersendtime_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersendtime',
            name='scheduled_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
