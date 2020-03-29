# Generated by Django 2.1.3 on 2020-03-24 17:21
 
from django.db import migrations
 
def addData(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    data = [
    ]
    Timeline = apps.get_model("timeline", "Timeline")
    timeline = [
        ("Financial Support", "0-4"),
        ("Financial Support", "4-11"),
        ("Financial Support", "11-18"),
        ("Financial Support", "18-25"),
        ("Educational Support", "0-4"),
        ("Educational Support", "4-11"),
        ("Educational Support", "11-18"),
        ("Educational Support", "18-25"),
        ("Governmental Support", "0-4"),
        ("Governmental Support", "4-11"),
        ("Governmental Support", "11-18"),
        ("Governmental Support", "18-25"),
        ("Charity Support Groups", "0-4"),
        ("Charity Support Groups","4-11"),
        ("Charity Support Groups","11-18"),
        ("Charity Support Groups", "18-25"),
        ("Therapy Support","0-4"),
        ("Therapy Support","4-11"),
        ("Therapy Support","11-18"),
        ("Therapy Support","18-25"),
        ("Transport Support","0-4"),
        ("Transport Support","4-11"),
        ("Transport Support","11-18"),
        ("Transport Support","18-25")
    ]
 
    for tl in timeline:
        t = Timeline(header = tl[0], age = tl[1])
        t.save()
 
class Migration(migrations.Migration):
    dependencies = [
        ('timeline', '0008_auto_20200324_2218'),
    ]

    operations = [
         migrations.RunPython(addData),
    ]