# Generated by Django 4.1 on 2022-09-03 14:11

from django.db import migrations


def load_products_from_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "products")


def delete_stores(apps, schema_editor):
    products = apps.get_model("products", "Products")
    products.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_products_user_alter_products_name_and_more'),
    ]

    operations = [
        migrations.RunPython(load_products_from_fixture, delete_stores),
    ]
