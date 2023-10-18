from django.shortcuts import render

from .models import Pizza
from .models import Bebida

def ProdutosView(request):
	
	pizza_lista = Pizza.objects.all()
	bebida_lista = Bebida.objects.all()
	return render(request, 'home.html', {'pizzas':pizza_lista, 'bebidas':bebida_lista})

