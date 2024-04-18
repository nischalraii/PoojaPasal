from django.db import models

from pooja.models import Product
from userauths.models import User


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    is_paid = models.BooleanField(default=False)


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    quantity = models.IntegerField(default=1, blank=False, null=False)

    @property
    def sub_total(self):
        return self.product.price * self.quantity


def item_count(user):
    return CartItems.objects.filter(cart__user=user).count()


def total_cost(user):
    items = CartItems.objects.filter(cart__user=user)
    total = 0
    for c in items:
        total += (c.product.price * c.quantity)
    return total
