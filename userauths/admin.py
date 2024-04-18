from django.contrib import admin
from .models import *
from pooja.models import *
from cart.models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_image', 'price', 'in_stock']


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'product_image1', 'product_image2', 'product_image3']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image', 'desc']


class CartAdmin(admin.ModelAdmin):
    list_display = ['user']


class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product']


admin.site.register(User, UserAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems, CartItemsAdmin)

