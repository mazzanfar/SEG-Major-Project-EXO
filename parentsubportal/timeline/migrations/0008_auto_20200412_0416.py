# Generated by Django 3.0.3 on 2020-04-12 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200410_0951'),
        ('timeline', '0007_auto_20200412_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='content',
            field=models.ManyToManyField(blank=True, null=True, related_name='contents', to='posts.Content'),
        ),
    ]
