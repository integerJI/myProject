# Generated by Django 2.1.8 on 2020-04-09 12:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0004_post_create_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_likes',
            field=models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]