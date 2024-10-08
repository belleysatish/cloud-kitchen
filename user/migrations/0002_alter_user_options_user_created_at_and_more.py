# Generated by Django 5.0.4 on 2024-05-06 19:01

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={},
        ),
        migrations.AddField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="last_updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="user",
            name="status",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="user",
            name="valid_till",
            field=models.DateField(
                default=datetime.datetime(
                    2025, 5, 6, 19, 1, 8, 260916, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterModelTable(
            name="user",
            table="USER",
        ),
    ]
