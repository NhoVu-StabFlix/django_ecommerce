from .models import Product, Category
from django.shortcuts import get_object_or_404,render


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def categories(request):
    return {
        'categories': Category.objects.all()

    }


def product_detail(request, slug):
    product=get_object_or_404(Product,slug=slug,in_stock=True)
    return render(request,'store/products/detail.html',{'product':product})
