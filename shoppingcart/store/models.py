from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(null=False ,max_length=50)
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    # on_sale
    # sale_discount
