# Generated by Django 3.0.3 on 2020-03-19 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0033_auto_20200319_0556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdf',
            name='test',
        ),
        migrations.AddField(
            model_name='pdf',
            name='pdf_file',
            field=models.FileField(default='null', upload_to='resources/pdfs/'),
            preserve_default=False,
        ),
    ]