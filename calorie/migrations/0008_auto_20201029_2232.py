# Generated by Django 3.1.2 on 2020-10-30 03:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calorie', '0007_auto_20201028_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyintake',
            name='intake_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 10, 30, 3, 32, 41, 917386, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='set_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 10, 30, 3, 32, 41, 917386, tzinfo=utc), null=True),
        ),
    ]
