# Generated by Django 3.0.3 on 2020-04-09 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='age',
            field=models.CharField(choices=[('0-4', '0-4'), ('4-11', '4-11'), ('11-18', '11-18'), ('18-25', '18-25'), ('N/A', 'N/A')], max_length=6),
        ),
    ]
