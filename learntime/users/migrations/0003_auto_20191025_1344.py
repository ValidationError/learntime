# Generated by Django 2.2.6 on 2019-10-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191009_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '管理员', 'verbose_name_plural': '管理员'},
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, '超级管理员'), (2, '校级'), (3, '院级'), (4, '干部级')], default=4, verbose_name='分配的身份'),
        ),
        migrations.AlterField(
            model_name='user',
            name='identity',
            field=models.IntegerField(choices=[(1, '超级管理员'), (2, '校级'), (3, '院级'), (4, '干部级')], default=1, verbose_name='请求的身份'),
        ),
    ]