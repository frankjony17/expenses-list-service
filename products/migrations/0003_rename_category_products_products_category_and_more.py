# Generated by Django 4.1 on 2022-08-30 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_table_alter_productscategory_table_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category',
            new_name='products_category',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='type',
            new_name='products_type',
        ),
    ]
