
from django.shortcuts import render
from .models import Compra
from .models import Pedido


def CompraView(request):
	
	compra_lista = Compra.objects.all()
	lista_pedido = Pedido.objects.all()
	
	return render(request, 'home.html', {'pizzas':compra_lista, 'pedido':lista_pedido})
	

