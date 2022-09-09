from django.contrib.auth.models import Permission

PERMISSIONS = [
    'add_products', 'change_products', 'delete_products', 'view_products', 'view_productscategory',
    'view_productstype', 'add_shopping', 'change_shopping', 'delete_shopping', 'view_shopping',
    'add_purchases', 'change_purchases', 'delete_purchases', 'view_purchases'
]


def post_save_add_user_permissions(sender, instance=None, created=False, **kwargs):
    if not instance.is_staff and created:
        for perm in PERMISSIONS:
            perm = Permission.objects.get(codename=perm)
            instance.user_permissions.add(perm)
            instance.save()
