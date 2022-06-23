# Generated by Django 3.2.9 on 2022-03-27 23:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speak', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('data', models.CharField(max_length=2084)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='speak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speak', models.CharField(max_length=225)),
            ],
        ),
    ]
