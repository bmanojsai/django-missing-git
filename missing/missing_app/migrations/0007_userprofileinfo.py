# Generated by Django 3.1.3 on 2021-07-21 04:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('missing_app', '0006_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_no', models.CharField(max_length=9, unique=True)),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('IT', 'IT'), ('ICT', 'ICT'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('EIE', 'EIE'), ('Mechanical', 'Mechanical'), ('Mechatronics', 'Mechatronics'), ('Civil', 'Civil'), ('Bio-Technology', 'Bio-Technology')], max_length=254)),
                ('mobile_no', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('id_card_pic', models.ImageField(upload_to='')),
                ('status', models.CharField(choices=[('Verified', 'Verified'), ('Not-Verified', 'Not-Verified')], default='Not-Verified', max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
