from django.apps import AppConfig
from django.db.models.signals import post_save


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_auth'

    def ready(self):
        from django.contrib.auth.models import User
        from .receivers import post_save_add_user_permissions
        post_save.connect(post_save_add_user_permissions, sender=User)
