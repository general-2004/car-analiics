from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Car(models.Model):
    BRAND_CHOICES = [
        ("BMW", "BMW"),
        ("Audi", "Audi"),
        ("Mercedes", "Mercedes"),
        ("Volkswagen", "Volkswagen"),
        ("Toyota", "Toyota"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("available", "В наявності"),
        ("sold", "Нема в наявності"),
        ("reserved", "Заброньовано"),
    ]

    name = models.CharField(max_length=30)
    brand = models.TextField(max_length=20)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()

    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    repair_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    transport_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default = "available"
    )

    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)