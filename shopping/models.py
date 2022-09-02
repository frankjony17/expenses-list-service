from django.db import models
from django.contrib.auth.models import User

from products.models import Products


class Shopping(models.Model):
    description = models.CharField(max_length=120, blank=False, null=False)
    purchase_date = models.DateField(blank=False, null=False)
    amount_available = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, default=0.00)
    approximate_cost = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, default=0.00)
    final_amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0.00)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="shopping", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "shopping"
        ordering = ['purchase_date']

    def __str__(self):
        return f"{self.description} - {str(self.purchase_date)}"


class Purchases(models.Model):
    quantity = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0.00)
    price_date = models.DateField(blank=True, null=True)
    checked = models.BooleanField(default=False, null=False)
    unit = models.IntegerField(blank=True, default='')
    products = models.ForeignKey(
        Products, related_name="purchases", on_delete=models.CASCADE, null=False, blank=False)
    shopping = models.ForeignKey(
        Shopping, related_name="purchases", on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "purchases"
        ordering = ['price']

    def __str__(self):
        return f"{self.products.name} - {self.price}"
