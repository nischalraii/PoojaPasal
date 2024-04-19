from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from pooja.models import *


# Create your views here.

def index(request):
    user = request.user
    if request.user.is_authenticated:
        return redirect("home")

    category = Category.objects.all()
    product = Product.objects.all()

    context = {
        'category': category,
        'user': user,
        'product': product,
    }

    return render(request, "index.html", context)


@login_required(redirect_field_name="")
def user_home(request):
    category = Category.objects.all()
    product = Product.objects.all()
    user = request.user

    context = {
        'category': category,
        'user': user,
        'product': product,
    }
    # if request.user.is_authenticated:
    return render(request, "user_home.html", context)


#   else:
#     messages.warning(request, "Please login first!")
#     return redirect("signin")

# @login_required(redirect_field_name="")
def view_category(request, cid):
    items = Product.objects.filter(category=cid)
    category = Category.objects.all()
    temp_cat = Category.objects.get(id=cid)

    context = {
        'items': items,
        'temp_cat': temp_cat,
        'category': category,
    }
    return render(request, 'category_products.html', context)


def product_details(request , pid):
    category = Category.objects.all()
    p_id =pid
    prdt = Product.objects.get(id= p_id)
    context = {
        'category': category,
        'product': prdt,
    }
    return render(request, "product_details.html", context)


def blog_details(request):
    return render(request, "blog-details.html")


def category_products(request, id):
    foods = Category.objects.filter(id=id)

    context = {
        'foods': foods
    }
    return render(request, "category_products.html", context)
