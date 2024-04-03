from django.db import models
import random

def generate_code():
    return ''.join(random.choices('0123456789', k=4))

class Item(models.Model):
    SLOT_CHOICES = [(i, str(i)) for i in range(1, 11)]

    code = models.CharField(max_length=4, unique=True, default=generate_code)
    title = models.CharField(max_length=255)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    link = models.CharField(max_length=1000)
    slot = models.IntegerField(null=True, blank=True, choices=SLOT_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100, default='N/A')
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.name