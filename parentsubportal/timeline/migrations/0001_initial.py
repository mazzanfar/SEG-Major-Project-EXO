# Generated by Django 3.0.3 on 2020-04-09 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('children', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(choices=[('Financial Support', 'Financial Support'), ('Educational Support', 'Educational Support'), ('Governmental Support', 'Governmental Support '), ('Charity Support Groups', 'Charity Support Groups'), ('Therapy Support', 'Therapy Support '), ('Transport Support', 'Transport Support ')], max_length=30)),
                ('age', models.CharField(choices=[('0-4', '0-4'), ('4-11', '4-11'), ('11-18', '11-18'), ('18-25', '18-25')], max_length=6)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='children.Children')),
            ],
        ),
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='timelinepdfs')),
                ('timeline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeline.Timeline')),
            ],
        ),
    ]
