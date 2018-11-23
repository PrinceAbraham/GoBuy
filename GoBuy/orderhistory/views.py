from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from product.models import Category, Product
from django.contrib.auth.models import User
from cart.models import Order

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        orders = Order.objects.filter(user_id=User.objects.get(username = request.user).id)
        products = []
        orderProducts = []
        for order in orders:
            for p in order.product.all():
                products.append(p)
            orderProducts.append(products)
            products = []
        args = {"orders": orders, "products": orderProducts}
        return render(request, 'order_history.html', args)
