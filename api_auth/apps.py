from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_auth'

    def ready(self):
        from . import receivers
        receivers.init_receiver()
