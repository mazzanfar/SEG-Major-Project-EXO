# Generated by Django 3.0.3 on 2020-04-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0008_auto_20200412_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='age',
            field=models.CharField(blank=True, choices=[('0-4', '0-4'), ('4-11', '4-11'), ('11-18', '11-18'), ('18-25', '18-25')], max_length=6),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='header',
            field=models.CharField(blank=True, choices=[('Financial Support', 'Financial Support'), ('Educational Support', 'Educational Support'), ('Governmental Support', 'Governmental Support '), ('Charity Support Groups', 'Charity Support Groups'), ('Therapy Support', 'Therapy Support '), ('Transport Support', 'Transport Support ')], max_length=30),
        ),
    ]
