# Generated by Django 5.1 on 2024-08-17 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LocationManagement', '0020_alter_regions_valid_till'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regions',
            name='valid_till',
            field=models.DateField(default=datetime.datetime(2025, 8, 17, 15, 22, 9, 35287, tzinfo=datetime.timezone.utc)),
        ),
    ]
