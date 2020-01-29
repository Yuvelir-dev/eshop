from django.urls import path

from .views import *
urlpatterns = [
	path('', posts_list, name='index'),
	path('product/<str:slug>/', product_page, name='product_page')

]