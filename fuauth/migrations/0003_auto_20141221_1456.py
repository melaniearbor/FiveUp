# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fuauth', '0002_auto_20141211_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=uuidfield.fields.UUIDField(unique=True, null=True, max_length=32, blank=True, editable=False),
            preserve_default=True,
        ),
    ]
