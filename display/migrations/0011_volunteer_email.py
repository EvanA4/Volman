# Generated by Django 5.1.4 on 2024-12-29 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("display", "0010_alter_volunteer_createdat"),
    ]

    operations = [
        migrations.AddField(
            model_name="volunteer",
            name="email",
            field=models.EmailField(default="undefined@gmail.com", max_length=255),
        ),
    ]
