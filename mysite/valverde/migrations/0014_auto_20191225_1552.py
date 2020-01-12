# Generated by Django 2.2.5 on 2019-12-25 14:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('valverde', '0013_auto_20191225_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_description',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 14, 52, 6, 527066, tzinfo=utc)),
        ),
    ]
