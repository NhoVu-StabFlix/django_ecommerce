from .models import Product, Category
from django.shortcuts import get_object_or_404, render


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/category.html', {'products': products})


def categories(request):
    return {
        'categories': Category.objects.all()

    }


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products=Product.objects.filter(category=category)
    return render(request,'store/products/category.html',{'category':category,'products':products})


