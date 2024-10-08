# Generated by Django 4.2.1 on 2024-06-17 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CloudKit', '0009_alter_category_valid_till_alter_foodstyle_valid_till_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='valid_till',
            field=models.DateField(default=datetime.datetime(2025, 6, 17, 16, 22, 5, 506687, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='foodstyle',
            name='valid_till',
            field=models.DateField(default=datetime.datetime(2025, 6, 17, 16, 22, 5, 506687, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='items',
            name='valid_till',
            field=models.DateField(default=datetime.datetime(2025, 6, 17, 16, 22, 5, 506687, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='meal',
            name='valid_till',
            field=models.DateField(default=datetime.datetime(2025, 6, 17, 16, 22, 5, 506687, tzinfo=datetime.timezone.utc)),
        ),
    ]
