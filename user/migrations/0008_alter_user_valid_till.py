# Generated by Django 4.2.1 on 2024-05-16 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_user_valid_till'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='valid_till',
            field=models.DateField(default=datetime.datetime(2025, 5, 16, 16, 23, 47, 458725, tzinfo=datetime.timezone.utc)),
        ),
    ]
