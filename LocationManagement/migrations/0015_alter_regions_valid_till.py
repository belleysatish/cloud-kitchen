# Generated by Django 4.2.1 on 2024-06-17 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LocationManagement', '0014_alter_regions_valid_till'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regions',
            name='valid_till',
            field=models.DateField(default=datetime.datetime(2025, 6, 17, 17, 12, 14, 918328, tzinfo=datetime.timezone.utc)),
        ),
    ]
