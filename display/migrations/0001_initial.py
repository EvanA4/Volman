# Generated by Django 5.1.4 on 2024-12-28 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("beganAt", models.DateTimeField()),
                ("length", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Volunteer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("age", models.IntegerField()),
                (
                    "createdAt",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 12, 28, 9, 42, 11, 140220)
                    ),
                ),
                ("sessions", models.ManyToManyField(to="display.session")),
            ],
        ),
    ]
