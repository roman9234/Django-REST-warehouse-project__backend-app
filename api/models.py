from django.contrib.auth.models import AbstractUser
from django.db import models



class ApiUser(AbstractUser):
    ...



# Наследуем от модели
class Warehouse(models.Model):
    name = models.CharField(max_length=128)


class Product(models.Model):
    name = models.CharField(max_length=128)


class Request(models.Model):
    product = models.ForeignKey(Product, related_name="requests", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    warehouse = models.ForeignKey(Warehouse, related_name="requests", on_delete=models.CASCADE)
    supplier = models.ForeignKey(ApiUser, related_name="supplier_requests", on_delete=models.CASCADE)
    # customer = models.ForeignKey(ApiUser, related_name="customer_requests", on_delete=models.CASCADE)


