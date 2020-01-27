# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("fuauth", "0002_auto_20141211_2035")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_joined",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date joined"
            ),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(
                unique=True, null=True, max_length=32, blank=True, editable=False
            ),
            preserve_default=True,
        ),
    ]
