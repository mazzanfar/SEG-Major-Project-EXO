# Generated by Django 2.1.7 on 2020-04-06 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthinfo',
            name='health_condition_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infos', to='health_data.HealthCondition'),
        ),
    ]
