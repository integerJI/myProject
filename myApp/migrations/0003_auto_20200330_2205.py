# Generated by Django 2.1.8 on 2020-03-30 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0002_post_update_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=200)),
                ('comment_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('comment_update_date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='date published')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myApp.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
