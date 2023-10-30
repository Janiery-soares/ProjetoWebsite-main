from django.shortcuts import render

from .models import DadosCliente


def CoreView(request):
	
	dados_clientes = DadosCliente.objects.all()
	
	return render(request, 'cadastro.html', {'clientes':dados_clientes,})