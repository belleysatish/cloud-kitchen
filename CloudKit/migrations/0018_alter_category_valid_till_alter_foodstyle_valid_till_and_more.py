# Generated by Django 5.1 on 2024-08-17 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CloudKit', '0017_alter_category_valid_till_alter_foodstyle_valid_till_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='valid_till',
            field=models.DateField(default=datetime.datetime(2025, 8, 17, 15, 44, 14, 974795, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='foodstyle',
            name='valid_till',
            field=models.DateField(default=datetime.datetime(2025, 8, 17, 15, 44, 14, 974795, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='items',
            name='valid_till',
            field=models.DateField(default=datetime.datetime(2025, 8, 17, 15, 44, 14, 974795, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='meal',
            name='valid_till',
            field=models.DateField(default=datetime.datetime(2025, 8, 17, 15, 44, 14, 974795, tzinfo=datetime.timezone.utc)),
        ),
    ]
