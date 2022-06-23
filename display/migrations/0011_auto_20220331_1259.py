# Generated by Django 3.2.9 on 2022-03-31 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('display', '0010_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='liked',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='display.blog')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
