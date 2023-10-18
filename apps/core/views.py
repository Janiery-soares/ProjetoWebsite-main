from django.shortcuts import render

from .models import Fornecedor
from .models import Produto

def FornecedorView(request):
	
	Fornecedor_lista = Fornecedor.objects.all()
	produto_lista = Produto.objects.all()
	return render(request, 'fornecedor.html', {'fornecedor':Fornecedor_lista, 'produtos':produto_lista})

