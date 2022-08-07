from django.shortcuts import render
from .models import *
# Create your views here.
# USING FUNCTION BASED VIEWS


def store(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        print(customer)
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        print(order)
        items = order.orderitem_set.all()
        print(items)
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, }
    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        print(customer)
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        print(order)
        items = order.orderitem_set.all()
        print(items)
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, }
    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'store/checkout.html', context)
