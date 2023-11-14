from django.shortcuts import render

from apps.produtos.models import *


def Home(request):
	
	pizzas = Pizza.objects.all()
	bebidas = Bebida.objects.all()
	drinks = Drinks.objects.all()
	return render(request, 'home.html', {'pizzas':pizzas, 'bebidas':bebidas, 'drinks':drinks})

	