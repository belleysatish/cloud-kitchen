# Generated by Django 5.1 on 2024-08-17 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_alter_user_valid_till_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='valid_till',
            field=models.DateField(default=datetime.datetime(2025, 8, 17, 15, 44, 14, 974795, tzinfo=datetime.timezone.utc)),
        ),
    ]
