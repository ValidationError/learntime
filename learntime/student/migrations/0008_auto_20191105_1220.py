# Generated by Django 2.2.6 on 2019-11-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_remove_student_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel_file', models.FileField(upload_to='student/%Y/%m/%d/', verbose_name='学生文件')),
            ],
            options={
                'verbose_name': '学生excel文件',
                'verbose_name_plural': '学生excel文件',
                'db_table': 'student_file',
            },
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('-credit',), 'verbose_name': '学生', 'verbose_name_plural': '学生'},
        ),
    ]
