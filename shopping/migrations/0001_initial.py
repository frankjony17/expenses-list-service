# Generated by Django 4.1 on 2022-09-01 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0005_products_user_alter_products_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=120)),
                ('purchase_date', models.DateField()),
                ('amount_available', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6)),
                ('approximate_cost', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6)),
                ('final_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'shopping',
                'ordering': ['purchase_date'],
            },
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6)),
                ('price_date', models.DateField(blank=True, null=True)),
                ('checked', models.BooleanField(default=False)),
                ('unit', models.IntegerField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='products.products')),
                ('shopping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='shopping.shopping')),
            ],
            options={
                'db_table': 'purchases',
                'ordering': ['price'],
            },
        ),
    ]