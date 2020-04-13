from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import signals
from django.apps import apps

Children = apps.get_model("children", "Children")
Timeline = apps.get_model("timeline", "Timeline")

""" On creation a child creates a corressponding timeline and populates it with initial content """
@receiver(signals.post_save, sender=Children)
def create_child(sender, instance, created, **kwargs):
    print("child is tested created")
    # raw is set when model is created from loaddata.
    timeline = Timeline(child=instance)
    timeline.save()
    # We initialize set up the timeline with all content for each disability that the user entered for the child
    for disability in instance.disabilities.all():
        print(disability.name)
        for c in disability.content.all():
            print(c.title)
            timeline.content.add(c)
    timeline.save()
