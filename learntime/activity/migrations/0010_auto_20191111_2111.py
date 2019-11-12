# Generated by Django 2.2.6 on 2019-11-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0009_auto_20191111_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='logo',
            field=models.ImageField(default='', upload_to='activity/logo/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='activity',
            name='place',
            field=models.CharField(default='', max_length=255, verbose_name='活动地点'),
        ),
    ]