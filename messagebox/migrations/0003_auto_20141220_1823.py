# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('messagebox', '0002_auto_20141220_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='messages'),
            preserve_default=True,
        ),
    ]
