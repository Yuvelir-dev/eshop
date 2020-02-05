from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe
import json
import os

# Create your views here.
@login_required
def checkout(request):
	

	return render(request, 'checkout.html', {})
