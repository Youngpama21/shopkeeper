from django.db import models

class Product(models.Model):
    product_no = models.CharField(max_length=100)
    product_name = models.CharField(max_length=200)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name

    @property
    def profit(self):
        return self.selling_price - self.buying_price
