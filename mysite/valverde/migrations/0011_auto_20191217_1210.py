# Generated by Django 2.2.5 on 2019-12-17 11:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('valverde', '0010_auto_20191217_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 11, 10, 42, 472316, tzinfo=utc)),
        ),
    ]
