from core.settings import DATE_FORMAT
from django.db import models


class Shopping(models.Model):
    description = models.CharField(max_length=120, blank=False, null=False)
    purchase_date = models.DateField(format=DATE_FORMAT, blank=False, null=False)
    amount_available = models.DecimalField(max_digits=6, decimal_places=2, blank=True,
                                           default=0.00)
    approximate_cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True,
                                           default=0.00)
    final_amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0.00)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "shopping"
        ordering = ['purchase_date']

    def __str__(self):
        return f"{self.description} - {str(self.purchase_date)}"


class Purchases(models.Model):
    quantity = models.IntegerField(blank=False, null=False)
