from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db.models import Model 
from django.shortcuts import reverse

# Create your models here.
class Product(models.Model):
	title_product = models.CharField(max_length=150, db_index=True)
	slug_product = models.SlugField(max_length=150, unique=True)
	description_product = models.TextField(blank=True, db_index=True)
	price_product = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)], blank=True, db_index=True)
	raiting_product =  models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, db_index=True)


	def __str__(self):
		return '{}'.format(self.title_product)
		
