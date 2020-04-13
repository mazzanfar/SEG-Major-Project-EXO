# Generated by Django 3.0.3 on 2020-04-12 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200410_0951'),
        ('timeline', '0004_auto_20200410_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='pdfs',
            field=models.ManyToManyField(to='posts.PDF'),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Topic'),
        ),
    ]