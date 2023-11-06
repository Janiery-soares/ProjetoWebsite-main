from django.shortcuts import render

from .models import DadosCliente


def Home(request):
	
	dados_clientes = DadosCliente.objects.all()
	return render(request, 'home.html', {'clientes':dados_clientes})

#def Cadastro():
	