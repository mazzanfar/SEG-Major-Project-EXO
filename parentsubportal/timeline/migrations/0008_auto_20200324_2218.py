# Generated by Django 3.0.3 on 2020-03-24 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0007_auto_20200321_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeline',
            old_name='ageRange',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='timeline',
            old_name='title',
            new_name='header',
        ),
    ]
