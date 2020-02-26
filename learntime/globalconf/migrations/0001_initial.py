# Generated by Django 2.2.6 on 2020-02-26 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.TextField(default='', verbose_name='系统公告')),
                ('is_maintenance', models.BooleanField(default=False, verbose_name='是否在维护')),
                ('criterion', models.FloatField(default=30, verbose_name='学时计算基准分数')),
            ],
            options={
                'verbose_name': '配置',
                'verbose_name_plural': '配置',
            },
        ),
    ]
