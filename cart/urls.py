from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from cart import views

urlpatterns =[
    path('cart/', views.cart, name="cart"),
    path('cart/<int:pid>/', views.delete_from_cart, name="delete_from_cart"),
    path('cart_add/<int:pid>/', views.add_to_cart, name="add_to_cart"),
    path('cart/<int:pid>/', views.change_quantity, name="change_quantity"),


]