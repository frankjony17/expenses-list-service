from django.db.models.signals import pre_save
from django.dispatch import receiver

from products.models import Products


@receiver(pre_save, sender=Products)
def pre_save_products_receiver(sender, instance, raw, using, **kwargs):
    if instance.user.is_staff or instance.user.is_superuser:
        # instance.user = None
        pass


pre_save.connect(pre_save_products_receiver, sender=Products)
