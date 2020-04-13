from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import signals
from django.apps import apps
from django.db import transaction
from .models import Timeline

@receiver(signals.post_save, sender=Timeline)
def create_child(sender, instance, created, **kwargs):
    print("timeline created")
