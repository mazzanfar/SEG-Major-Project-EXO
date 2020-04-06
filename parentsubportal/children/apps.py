from django.apps import AppConfig


class ChildrenConfig(AppConfig):
    name = 'children'

    def ready(self):
        from . import signals
