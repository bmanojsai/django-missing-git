# Generated by Django 3.1.3 on 2021-08-01 04:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missing_app', '0014_auto_20210801_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items_lost',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 1, 10, 26, 43, 225144)),
        ),
    ]
