# Generated by Django 3.0.3 on 2020-02-26 17:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200226_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Article type',
                'verbose_name_plural': 'Article types',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_posted']},
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.BigIntegerField(default=0),
        ),
    ]