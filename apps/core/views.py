from django.shortcuts import render

from .models import Fornecedor
from .models import Produto


def FornecedorView(request):
	
	dados_fornecedor = Fornecedor.objects.all()
    dados_produtos = Produto.objects.all()
	
	return render(request, 'fornecedor.html', {'fornecedor': dados_fornecedor, 'produtos':dados_produtos})
