from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from product.models import Product
from django.urls import reverse
from shop.models import Transaction
from django.contrib.auth.models import User
from .models import Order
import random

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        transactions = Transaction.objects.filter(user_id = User.objects.get(username = request.user).id)
        total = 0
        for t in transactions:
            total += t.product.price
        args = {"transactions": transactions, "total": total}
        return render(request, 'cart.html', args)

def remove_from_cart(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    transaction = Transaction.objects.get(user=request.user, product_id= product.id)
    # transaction = Transaction(user = User.objects.get(username=request.user),
    # product = product,
    # status = "add")
    # transaction.save()
    transaction.delete()
    #update product count
    product.quantity = product.quantity+1
    product.save(update_fields=['quantity'])
    return redirect(reverse('cart:home'))

def place_order(request, **kwargs):
    transactions = Transaction.objects.filter(user_id = User.objects.get(username = request.user).id)
    products = []
    total = 0
    order_number = random.randint(1000000000,9999999999)
    for t in transactions:
        products.append(t.product)
    for t in transactions:
        total += t.product.price
    order = Order(user_id=User.objects.get(username=request.user).id,
    total=total,
    order_number=order_number)
    order.save()
    order.product.set(products)
    order.save()
    #remove transactions
    for t in transactions:
        t.delete()
    
    return redirect(reverse('cart:home'))
