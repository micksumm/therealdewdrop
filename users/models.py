from django.db import models
from django.contrib.auth.models import User

from products.models import Product

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'