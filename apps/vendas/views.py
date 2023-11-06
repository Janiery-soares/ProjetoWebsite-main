
from django.shortcuts import render

from .models import Pedido


def CompraView(request):
	
	lista_pedido = Pedido.objects.all()
	
	return render(request, 'compra.html', {'pedido':lista_pedido})
	

