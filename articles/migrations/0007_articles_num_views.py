# Generated by Django 4.2.3 on 2023-08-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_articles_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='num_views',
            field=models.IntegerField(default=0),
        ),
    ]
