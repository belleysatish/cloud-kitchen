# Generated by Django 5.0.4 on 2024-05-06 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("LocationManagement", "0002_alter_regions_valid_till"),
    ]

    operations = [
        migrations.AlterField(
            model_name="regions",
            name="valid_till",
            field=models.DateField(
                default=datetime.datetime(
                    2025, 5, 6, 19, 7, 27, 988452, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
