# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CuratedMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('message_text', models.TextField(max_length=125)),
                ('message_author_first', models.TextField(max_length=35)),
                ('message_author_last', models.TextField(max_length=35)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
