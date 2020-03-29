# Generated by Django 3.0.3 on 2020-03-19 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0032_auto_20200319_0443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdf',
            name='pdf_file',
        ),
        migrations.AddField(
            model_name='pdf',
            name='test',
            field=models.IntegerField(blank=True, default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pdf',
            name='lower_age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='upper_age',
            field=models.IntegerField(blank=True),
        ),
    ]