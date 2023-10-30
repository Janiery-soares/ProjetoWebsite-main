
from django.shortcuts import render

from .models import Pedido


def CompraView(request):
	
	lista_pedido = Pedido.objects.all()
	
	return render(request, 'home.html', {'pedido':lista_pedido})
	

