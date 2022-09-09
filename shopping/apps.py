from django.apps import AppConfig
from django.db.models.signals import post_save


class ShoppingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopping'

    def ready(self):
        from .receivers import post_save_update_price_date_receiver
        post_save.connect(post_save_update_price_date_receiver, sender='shopping.Purchases')
