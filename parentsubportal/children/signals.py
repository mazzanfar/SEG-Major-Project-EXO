from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import signals
from django.apps import apps

Children = apps.get_model("children", "Children")
Timeline = apps.get_model("timeline", "Timeline")

@receiver(signals.post_save, sender=Children)
def create_child(sender, instance, created, **kwargs):
    print("child is tested created")
    # raw is set when model is created from loaddata.
    if created:
        Timeline.objects.create(header = "Financial Support", age = "0-4", child =instance)
        Timeline.objects.create(header = "Financial Support", age = "4-11",child=instance)
        Timeline.objects.create(header = "Financial Support", age = "11-18",child=instance)
        Timeline.objects.create(header = "Financial Support", age = "18-25",child=instance)

        Timeline.objects.create(header = "Educational Support", age = "0-4",child=instance)
        Timeline.objects.create(header = "Educational Support", age = "4-11",child=instance)
        Timeline.objects.create(header = "Educational Support", age = "11-18",child=instance)
        Timeline.objects.create(header = "Educational Support", age = "18-25",child=instance)

        Timeline.objects.create(header = "Governmental Support", age = "0-4",child=instance)
        Timeline.objects.create(header = "Governmental Support", age = "4-11",child=instance)
        Timeline.objects.create(header = "Governmental Support", age = "11-18",child=instance)
        Timeline.objects.create(header = "Governmental Support", age = "18-25",child=instance)

        Timeline.objects.create(header = "Charity Support Groups", age = "0-4",child=instance)
        Timeline.objects.create(header = "Charity Support Groups", age = "4-11",child=instance)
        Timeline.objects.create(header = "Charity Support Groups", age = "11-18",child=instance)
        Timeline.objects.create(header = "Charity Support Groups", age = "18-25",child=instance)

        Timeline.objects.create(header = "Therapy Support", age = "0-4",child=instance)
        Timeline.objects.create(header = "Therapy Support", age = "4-11",child=instance)
        Timeline.objects.create(header = "Therapy Support", age = "11-18",child=instance)
        Timeline.objects.create(header = "Therapy Support", age = "18-25",child=instance)

        Timeline.objects.create(header = "Transport Support", age = "0-4",child=instance)
        Timeline.objects.create(header = "Transport Support", age = "4-11",child=instance)
        Timeline.objects.create(header = "Transport Support", age = "11-18",child=instance)
        Timeline.objects.create(header = "Transport Support", age = "18-25",child=instance)
