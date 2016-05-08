# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuauth', '0009_auto_20160507_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='how_many_messages',
            field=models.CharField(default=5, max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')]),
            preserve_default=True,
        ),
    ]
