# Generated by Django 3.0.3 on 2020-03-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0005_delete_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='fetcheddata',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
