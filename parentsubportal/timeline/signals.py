from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import Children
from .models import Timeline

@receiver(post_save, sender=Children)
def init_new_child(instance, created, raw, **kwargs):
    # raw is set when model is created from loaddata.
    if created and not raw:
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
