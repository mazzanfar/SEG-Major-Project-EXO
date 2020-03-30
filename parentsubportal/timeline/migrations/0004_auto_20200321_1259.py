# Generated by Django 3.0.3 on 2020-03-21 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0037_auto_20200315_1013'),
        ('timeline', '0003_auto_20200321_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='pdfs',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='pdfs', to='posts.PDF'),
        ),
    ]
