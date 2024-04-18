from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from cart.models import Cart, CartItems, item_count, total_cost
from pooja.models import Product, Category


# Create your views here.

def cart(request):
    n_cart = Cart.objects.get(user=request.user)
    items = CartItems.objects.filter(cart=n_cart)
    category = Category.objects.all()
    count = item_count(request.user)
    total = total_cost(request.user)

    if request.method == "POST":
        quantity = request.POST.get("quantity")
        proid = request.POST.get("proid")
        print(proid)
        prod = Product.objects.get(id=proid)
        cart = Cart.objects.get(user=request.user)
        the_item = CartItems.objects.filter(cart= cart, product= prod)
        the_item.update(quantity=quantity)

    context = {
        'cart': n_cart,
        'items': items,
        'category': category,
        'count':count,
        'total': total,
    }
    return render(request, "cart.html", context)


def add_to_cart(request, pid):
    prod = Product.objects.get(id=pid)
    user = request.user

    temp_cart = Cart.objects.get(user=user)
    if temp_cart:
        pass
    else:
        temp_cart = Cart.objects.create(user=user)
        temp_cart.save()

    cart_item = CartItems.objects.create(cart=temp_cart, product=prod)
    if cart_item is not None:
        cart_item.save()
        messages.success(request, "Item added to cart successfully!")
    else:
        messages.warning(request, "Opps! Something went wrong.")

    return HttpResponseRedirect('/')


def delete_from_cart(request, pid):
    cart = Cart.objects.get(user=request.user)
    product = Product.objects.get(id= pid)
    item = CartItems.objects.get(cart=cart, product=product)
    if item:
        item.delete()
        messages.success(request, "Item removed from cart successfully!")
    else:
        messages.warning(request, "Opps! Something went wrong.")

    return HttpResponseRedirect('/cart/')

def change_quantity(request, pid):
    if request.method == "POST":
        quantity = request.POST.get('quantity')
        product = Product.objects.get(id=pid)
        itm = CartItems.objects.get(user= request.user, product= product).update(quantity=quantity)
        itm.save()

    return HttpResponseRedirect('/cart/')




