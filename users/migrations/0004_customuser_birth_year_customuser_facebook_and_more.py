# Generated by Django 4.2.3 on 2023-08-17 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_user_name_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birth_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='facebook',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='customuser',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='customuser',
            name='number_phone',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='customuser',
            name='tiktok',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
