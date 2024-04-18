from django.db import models
from django.utils.safestring import mark_safe

from userauths.models import User


# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.user.id, filename)


class Category(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    image = models.ImageField(upload_to="Category", default="nothing.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50",height= "50"/>' % self.image.url)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="Product", default="nothing.jpg")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    in_stock = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50",height= "50"/>' % self.image.url)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image1 = models.ImageField(upload_to="product-images", default="nothing.jpg")
    image2 = models.ImageField(upload_to="product-images", default="nothing.jpg")
    image3 = models.ImageField(upload_to="product-images", default="nothing.jpg")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Product-Images"

    def product_image1(self):
        return mark_safe('<img src="%s" width="50",height= "50"/>' % self.image1.url)

    def product_image2(self):
        return mark_safe('<img src="%s" width="50",height= "50"/>' % self.image2.url)

    def product_image3(self):
        return mark_safe('<img src="%s" width="50",height= "50"/>' % self.image3.url)

    def __str__(self):
        return self.product.name + "images"


    
