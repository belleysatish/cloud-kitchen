# Generated by Django 4.2.1 on 2024-05-19 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LocationManagement', '0009_alter_regions_valid_till'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regions',
            name='valid_till',
            field=models.DateField(default=datetime.datetime(2025, 5, 19, 8, 41, 37, 769870, tzinfo=datetime.timezone.utc)),
        ),
    ]
