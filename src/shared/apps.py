from django.apps import AppConfig


class SharedConfig(AppConfig):
    name = 'shared'
    label = 'shared'

    def ready(self):
        from shared.infrastructure.dependencies import configure_injector

        configure_injector()
