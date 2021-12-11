from django.apps import AppConfig


class PayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pay'

    def ready(self):
        # import signal handlers
        import pay.signals
