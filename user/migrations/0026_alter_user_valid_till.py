# Generated by Django 5.1 on 2024-08-17 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_alter_user_valid_till'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='valid_till',
            field=models.DateField(default=datetime.datetime(2025, 8, 17, 15, 52, 26, 240140, tzinfo=datetime.timezone.utc)),
        ),
    ]
