# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("auth", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        serialize=False,
                        primary_key=True,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        verbose_name="superuser status",
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, null=True, max_length=35, verbose_name="your name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        unique=True, max_length=255, verbose_name="your email address"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(max_length=10, verbose_name="your phone number"),
                ),
                (
                    "carrier",
                    models.CharField(
                        choices=[
                            ("ATT", "AT\\&T"),
                            ("VZ", "Verizon"),
                            ("VG", "Virgin"),
                        ],
                        default="VG",
                        max_length=2,
                    ),
                ),
                (
                    "timezone",
                    models.CharField(
                        choices=[
                            ("HI", "Hawaii"),
                            ("AK", "Alaska"),
                            ("PC", "Pacific"),
                            ("MT", "Mountain"),
                            ("CN", "Central"),
                            ("EA", "Eastern"),
                            ("AT", "Atlantic"),
                        ],
                        default="PC",
                        max_length=2,
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        verbose_name="staff status",
                        help_text="Designates whether the user can log into this admin        site",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=False,
                        verbose_name="active",
                        help_text="Designates whether the user should be treated as active.        Unselect this instead of deleting accounts.",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(verbose_name="date joined", auto_now=True),
                ),
                ("receive_newsletter", models.BooleanField(default=False)),
                (
                    "uuid",
                    models.UUIDField(
                        editable=False, unique=True, max_length=32, blank=True
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        related_query_name="user",
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of his/her group.",
                        related_name="user_set",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        related_query_name="user",
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={"abstract": False},
            bases=(models.Model,),
        )
    ]
