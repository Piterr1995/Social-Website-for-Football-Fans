# Generated by Django 2.2.5 on 2019-12-25 17:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('valverde', '0015_auto_20191225_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 17, 25, 23, 736419, tzinfo=utc)),
        ),
    ]
