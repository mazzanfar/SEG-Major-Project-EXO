# Generated by Django 3.0.3 on 2020-03-15 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_post_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
    ]