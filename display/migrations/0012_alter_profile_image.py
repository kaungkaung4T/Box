# Generated by Django 3.2.9 on 2022-04-07 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0011_auto_20220331_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='photo.jpg', upload_to='media'),
        ),
    ]