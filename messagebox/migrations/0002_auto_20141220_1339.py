# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("fuauth", "0001_initial"), ("messagebox", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="recipient",
            field=models.ForeignKey(
                to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
            ),
            preserve_default=True,
        )
    ]
