# Generated by Django 3.0.3 on 2020-02-27 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
