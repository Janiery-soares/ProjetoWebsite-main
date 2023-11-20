from django.shortcuts import render, redirect
from .forms import LoginForms
from .models import DadosCliente
from django.contrib.auth import authenticate, login


def Home(request):
	
	dados_clientes = DadosCliente.objects.all()
	return render(request, 'home.html', {'clientes':dados_clientes})

def Login(request):
	if request.method == 'POST':
		form = LoginForms(request.POST)
		if form.is_valid():
			nome_usuario = form.cleaned_data['username']
			senha = form.cleaned_data['password']
			user = authenticate(request,username=nome_usuario,password=senha)
			if user is not None:
				login(request,user)
				return redirect('home')
			else: 
				form.add_error(None, 'tente novamente')
	else:
		form = LoginForms()
    return render(request,'login.html', {'form':form})
   