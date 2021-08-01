# Generated by Django 3.1.3 on 2021-07-29 02:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('missing_app', '0008_auto_20210725_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items_lost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=254)),
                ('item_details', models.TextField()),
                ('expected_place', models.CharField(default='None', max_length=254)),
                ('item_pic', models.ImageField(blank=True, upload_to='')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]