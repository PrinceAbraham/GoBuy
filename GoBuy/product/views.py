from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ProductForm, CategoryForm
from .models import Category, Product

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        productForm = ProductForm
        categoryForm = CategoryForm
        categories = Category.objects.all()
        products = Product.objects.all()
        categories = Category.objects.all()
        args = {'p_form': productForm, 'c_form': categoryForm, 'categories': categories, 'products': products}
        return render(request, 'product.html', args)

    def post(self, request, **kwargs):
        productForm = ProductForm
        categoryForm = CategoryForm
        categories = []
        products = []
        if 'product-form' in request.POST:
            product = Product(
            name = request.POST.get("name"),
            slug = request.POST.get("slug"),
            price = request.POST.get("price"),
            quantity = request.POST.get("quantity"),
            category = Category.objects.get(id=request.POST.get("category")),
            image_url = request.POST.get("image_url"))
            product.save()
            return redirect("product.html")
        if 'category-form' in request.POST:
            category = Category(name = request.POST.get("name"))
            category.save()
            return redirect("product.html")
        args = {'p_form': productForm, 'c_form': categoryForm, 'categories': categories, 'products': products}
        return render(request, 'product.html', args)
