# Generated by Django 3.1.3 on 2021-08-01 04:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missing_app', '0011_auto_20210731_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='items_lost',
            name='emaill',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='items_lost',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 1, 9, 49, 21, 181728)),
        ),
    ]