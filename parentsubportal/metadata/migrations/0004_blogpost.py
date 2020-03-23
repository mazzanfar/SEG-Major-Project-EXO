# Generated by Django 2.1.7 on 2020-03-23 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0003_delete_beer'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('short_text', models.TextField()),
                ('posted_at', models.DateTimeField()),
            ],
        ),
    ]
