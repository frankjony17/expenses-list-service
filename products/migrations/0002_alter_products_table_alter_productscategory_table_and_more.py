# Generated by Django 4.1 on 2022-08-30 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='products',
            table='products',
        ),
        migrations.AlterModelTable(
            name='productscategory',
            table='products_category',
        ),
        migrations.AlterModelTable(
            name='productstype',
            table='products_type',
        ),
    ]
