# Generated by Django 2.2.5 on 2019-12-25 18:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('valverde', '0019_auto_20191225_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 18, 31, 43, 669974, tzinfo=utc)),
        ),
    ]
