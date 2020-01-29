from django.shortcuts import render
from .models import Product

# Create your views here.
def posts_list(request):
	products = Product.objects.all()
	return render(request, 'eshop_site/index.html', {'products': products})

def product_page(request, slug):
	product = Product.objects.get(slug_product=slug)
	return render(request, 'eshop_site/product_page.html', context={'product': product})