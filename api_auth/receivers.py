from django.contrib.auth.models import Permission, User
from django.db.models.signals import post_save
from django.dispatch import receiver

PERMISSIONS = [
    'add_products', 'change_products', 'delete_products', 'view_products', 'view_productscategory',
    'view_productstype', 'add_shopping', 'change_shopping', 'delete_shopping', 'view_shopping',
    'add_purchases', 'change_purchases', 'delete_purchases', 'view_purchases'
]


@receiver(post_save, sender=User)
def add_user_permissions(sender, instance=None, created=False, **kwargs):
    if not instance.is_staff and created:
        for perm in PERMISSIONS:
            perm = Permission.objects.get(codename=perm)
            instance.user_permissions.add(perm)
            instance.save()


# pre_save.connect(add_user_permissions, sender=User)


def init_receiver():
    print("User receiver initialized OK... (Put Logs TODO)")  # TODO: add logs.
