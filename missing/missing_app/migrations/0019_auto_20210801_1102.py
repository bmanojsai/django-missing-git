# Generated by Django 3.1.3 on 2021-08-01 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missing_app', '0018_auto_20210801_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items_lost',
            name='item_pic',
        ),
        migrations.AlterField(
            model_name='items_lost',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]