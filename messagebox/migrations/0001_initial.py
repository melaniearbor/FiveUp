# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('recipient', models.CharField(max_length=32)),
                ('sender_name', models.CharField(max_length=35)),
                ('message_text', models.TextField(max_length=125)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('message_sent', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
