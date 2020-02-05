from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import Count
import stripe


# Create your views here.
def posts_list(request):
	products = Product.objects.all()
	return render(request, 'eshop_site/index.html', {'products': products})

def product_page(request, slug):
	product = Product.objects.get(slug_product=slug)
	return render(request, 'eshop_site/product_page.html', context={'product': product})


def profile(request):
	user = User.objects.get()
	card = Card.objects.filter(user_name=user.username, pay=True)
	if request.user.is_authenticated:
		return render(request, 'eshop_site/profile.html', context={'user': user, 'card': card})
	else:
		return redirect('/')

def Add_card(request):
	if request.method == 'GET':
		id_product = request.GET.get('id')
		product = Product.objects.get(id=id_product)
		user = User.objects.get(id=request.user.id)
		card = Card.objects.all().filter(user_name = user.username, title_product=product.title_product, pay=False).first()

		if card != None:
			card.count += 1
			card.save()
		else:
			card = Card()
			card.user_name = user.username
			card.title_product = product.title_product
			card.price_product = product.price_product
			card.product = product
			card.save()
		return HttpResponse('ok')
		
def order(request):
	if request.method == "DELETE":
		id = request.GET.get('id')
		card = Card.objects.get(id=id)
		card.delete()
		return HttpResponse('deleted')
	if request.method == 'GET':
		user = User.objects.get(id=request.user.id)
		card = Card.objects.filter(user_name=user.username, pay=False)
		delivery = Delivery_method.objects.all()

		return render(request, 'eshop_site/order.html', context={'card': card, 'user': user, 'delivery': delivery})
	if request.method == 'POST':
		user = User.objects.get(id=request.user.id)
		delivery_methods = request.POST.get('delivery_method')
		card = Card.objects.filter(user_name=user.username, pay=False)
		for x in card:
			x.delivery_method = delivery_methods
			x.save()
		

		
		
		title = Card.objects.all().filter(user_name=user.username).first()
		
		fcost = 0
		for i in card:
			cost = i.price_product * i.count * 100
			fcost += cost

		if fcost == 0:
			return HttpResponse('invalid payment')

		stripe.api_key = 'sk_test_VplqTsmvH7pR9oqe0VHfgrNX00r8eLUW2F'

		session = stripe.checkout.Session.create(
		payment_method_types=['card'],
		line_items=[{
		'name': title,
		'description': 'Comfortable cotton t-shirt',
		'images': [title.product.image.url],
		'amount': fcost,
		'currency': 'usd',
		'quantity': 1,
		}],
		success_url='http://localhost:8000/success?session_id={CHECKOUT_SESSION_ID}"',
		cancel_url='http://localhost:8000/odrer',
		)
		return HttpResponse(session['id'])
			# order.delivery_method = 
def success(request):
	session_id = request.GET.get('session_id')
	if session_id:
		user = User.objects.get(id=request.user.id)
		card = Card.objects.filter(user_name=user.username)
		for x in card:
			x.pay = True
			x.save()
		return render(request, 'eshop_site/order.html')
	else:
		return redirect('/')

def add_cat(request):
	if request.method == 'GET':
		add_cat = Categories.objects.all()
		return render(request, 'eshop_site/add_cat.html', context={'add_cat': add_cat})
	if request.method == 'POST':			
		add_cat = Categories()
		title_category = request.POST.get('categories_title')
		id_category = request.POST.get('id_cat')
		add_cat.categories_title = title_category
		add_cat.id_cat = id_category
		add_cat.save()
		return HttpResponse('Dobavil')