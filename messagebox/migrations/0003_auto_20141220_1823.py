# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("messagebox", "0002_auto_20141220_1339")]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="recipient",
            field=models.ForeignKey(
                to=settings.AUTH_USER_MODEL,
                related_name="messages",
                on_delete=models.CASCADE,
            ),
            preserve_default=True,
        )
    ]
