from django.contrib.auth.models import User, Permission
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

PERMISSIONS = [
    'add_products', 'change_products', 'delete_products', 'view_products', 'view_productscategory',
    'view_productstype'
]


@receiver(post_save, sender=User)
def add_permissions(sender, instance=None, created=False, **kwargs):
    if not instance.is_staff and created:
        for perm in PERMISSIONS:
            perm = Permission.objects.get(codename=perm)
            instance.user_permissions.add(perm)
            instance.save()


pre_save.connect(add_permissions, sender=User)


def init_receiver():
    print("User receiver initialized OK... (Put Logs TODO)")
