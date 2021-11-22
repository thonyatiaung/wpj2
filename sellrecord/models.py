from django.db import models

# Create your models here.

class sellrecord(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=11)
    purchase_item = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    showroom = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return self.customer_name

