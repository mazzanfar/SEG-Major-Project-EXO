# Generated by Django 3.0.3 on 2020-03-15 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0036_auto_20200315_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pdf',
            old_name='topic',
            new_name='topics',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='topic',
            new_name='topics',
        ),
    ]
