# Generated by Django 3.0.3 on 2020-04-13 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_disability_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='disabilities',
            field=models.ManyToManyField(blank=True, null=True, related_name='content', to='posts.Disability'),
        ),
        migrations.AlterField(
            model_name='content',
            name='topics',
            field=models.ManyToManyField(null=True, related_name='topics', to='posts.Topic'),
        ),
    ]
