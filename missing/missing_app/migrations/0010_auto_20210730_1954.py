# Generated by Django 3.1.3 on 2021-07-30 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('missing_app', '0009_items_lost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items_lost',
            old_name='email',
            new_name='usernamee',
        ),
    ]
