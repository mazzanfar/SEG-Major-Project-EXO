# Generated by Django 3.0.3 on 2020-04-12 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_content_content_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='content_type',
        ),
    ]