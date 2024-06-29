from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/home.html', context)


def details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/detail.html', context={'product': product})
