from django.urls import path
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from .views import *
from checkout import views as checkout_views # new



urlpatterns = [
	path('', posts_list, name='index'),
	path('profile/', profile, name='profile'),
	path('order/', order, name='order'),
	path('card/', Add_card, name='card'),
	path('product/<str:slug>/', product_page, name='product_page'),
	path('success/', success, name='success'),
	path('add_cat/', add_cat, name='add_cat'),

]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
