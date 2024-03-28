# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    shop_location = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.shop_name


class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.warehouse_name


class Product(models.Model):
    product_name = models.CharField(max_length=100, null=True)
    price = models.PositiveIntegerField(null=True)
    quantity = models.PositiveIntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return str(self.product_name)


class Student(models.Model):
    student_name = models.CharField(max_length=50, null=True)
    student_class = models.CharField(max_length=10, null=True)
    profile_pic = models.ImageField(upload_to='student_profiles/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return str(self.student_name)
