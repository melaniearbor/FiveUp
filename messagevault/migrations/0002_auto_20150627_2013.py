# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messagevault', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curatedmessage',
            name='message_author_first',
            field=models.CharField(max_length=35),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='curatedmessage',
            name='message_author_last',
            field=models.CharField(max_length=35),
            preserve_default=True,
        ),
    ]
