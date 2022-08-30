from django.db import models


class ProductsType(models.Model):
    type = models.CharField(max_length=120, blank=False)
    description = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products_type"
        ordering = ['type']

    def __str__(self):
        return self.type


class ProductsCategory(models.Model):
    category = models.CharField(max_length=120, blank=False)
    description = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products_category"
        ordering = ['category']

    def __str__(self):
        return self.category


class Products(models.Model):
    name = models.CharField(max_length=120, blank=False)
    thumbnail = models.CharField(max_length=120, blank=True, default='')
    description = models.TextField(blank=True, default='')
    estimated_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    products_type = models.ForeignKey(ProductsType, related_name="products", on_delete=models.SET_NULL, null=True)
    products_category = models.ForeignKey(ProductsCategory, related_name="products", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "products"
        ordering = ['name']
