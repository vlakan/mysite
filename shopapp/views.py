from django.shortcuts import render
from django.http import HttpRequest
from timeit import default_timer
from random import randint

from .models import Product, Order


def shop_index(request: HttpRequest):
    digits = [randint(1, 9) for _ in range(3)]
    products = [
        ('Laptop', 1999),
        ('Desktop', 2999),
        ('Smartphone', 999)
    ]
    context = {
        "time_running": default_timer(),
        "products": products,
        "digits": digits,
    }
    return render(request, 'shopapp/shop-index.html', context=context)


def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)


def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related("products").all(),
    }
    return render(request, 'shopapp//orders-list.html', context=context)
