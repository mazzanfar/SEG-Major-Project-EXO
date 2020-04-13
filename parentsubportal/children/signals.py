from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import signals
from django.apps import apps

Children = apps.get_model("children", "Children")
Timeline = apps.get_model("timeline", "Timeline")
Content = apps.get_model("posts", "Content")

@receiver(signals.post_save, sender=Children)
def create_child(sender, instance, created, **kwargs):
    print("child is tested created")
    # raw is set when model is created from loaddata.
    timeline = Timeline(child=instance)
    timeline.save()
    content = Content.objects.all()
    timeline.content.add(*content)
    timeline.save()
