# Generated by Django 4.1.1 on 2022-09-09 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_owner_products_user'),
        ('shopping', '0004_alter_purchases_price_alter_purchases_quantity'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='purchases',
            unique_together={('shopping', 'products')},
        ),
    ]
