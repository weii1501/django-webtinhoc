# Generated by Django 4.2.3 on 2023-08-14 10:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('replies', '0002_reply_is_solved'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='num_point',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reply',
            name='vote',
            field=models.ManyToManyField(blank=True, related_name='replies_voted', to=settings.AUTH_USER_MODEL),
        ),
    ]
