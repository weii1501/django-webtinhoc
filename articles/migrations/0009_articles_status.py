# Generated by Django 4.2.3 on 2023-08-17 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_articles_num_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='status',
            field=models.CharField(choices=[('C', 'Đang chờ'), ('P', 'Công khai'), ('B', 'Cấm')], default='C', max_length=1),
        ),
    ]
