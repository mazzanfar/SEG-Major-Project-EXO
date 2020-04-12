# Generated by Django 3.0.3 on 2020-04-12 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('posts', '0004_auto_20200410_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
