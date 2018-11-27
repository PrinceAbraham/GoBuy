from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from product.models import Product
from django.urls import reverse
from .models import Transaction
from django.contrib.auth.models import User

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        products = Product.objects.all()
        transactions = Transaction.objects.filter(user_id = User.objects.get(username = request.user))
        for t in transactions:
            for index, p in enumerate(products):
                if t.product_id == p.id:
                    products[index].transaction = t

        args = {"products": products, "transactions": transactions}
        return render(request, 'shop.html', args)

def add_to_cart(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    if product.quantity > 0:
        transaction = Transaction(user = User.objects.get(username=request.user),
        product = product,
        status = "add")
        transaction.save()
        #update product count
        product.quantity = product.quantity-1
        product.save(update_fields=['quantity'])
    return redirect(reverse('shopping_cart:home'))

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
    return redirect(reverse('shopping_cart:home'))
