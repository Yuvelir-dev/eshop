from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db.models import Model 
from django.shortcuts import reverse
from django.utils.text import slugify 
from django.contrib.auth.models import User
from time import time

def gen_slug(s):
	new_slug = slugify(s, allow_unicode=True)
	return new_slug + '-' + str(int(time()))

class EShopUser(User):
	"""docstring for User"""
	def __init__(self, arg):
		super(User, self).__init__()
		self.arg = arg
		
class Categories(models.Model):
	categories_title = models.CharField(max_length=150, db_index=True)
	id_cat = models.PositiveIntegerField(blank=True, default=0)
	def __str__(self):
		return self.categories_title


# Create your models here.
class Product(models.Model):
	title_product = models.CharField(max_length=150, db_index=True)
	slug_product = models.SlugField(max_length=150, blank=True, unique=True)
	description_product = models.TextField(blank=True, db_index=True)
	price_product = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)], blank=True, db_index=True)
	raiting_product =  models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, db_index=True)
	image = models.ImageField(upload_to='images/')
	categories = models.ForeignKey('Categories', null=True, blank=True, on_delete=models.CASCADE)
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug_product = gen_slug(self.title_product)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title_product


class Delivery_method(models.Model):
	delivery_method = models.CharField(max_length=150, db_index=True)
	delivery_cost = models.PositiveIntegerField(db_index=True, default=0)
	"""docstring for delivery_method"""


class Card(models.Model):
	pay = models.BooleanField(default=False)
	product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='rel_product')
	count = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0)], blank=True, db_index=True)
	title_product = models.CharField(max_length=150, db_index=True)
	user_name = models.CharField(max_length=150, db_index=True)
	price_product = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)], blank=True, db_index=True)
	delivery_method = models.CharField(max_length=150, db_index=True)

	
class Order(models.Model):
	count = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0)], blank=True, db_index=True)
	title_product = models.CharField(max_length=150, db_index=True)
	user_name = models.CharField(max_length=150, db_index=True)
	delivery_method = models.CharField(max_length=150, db_index=True)

