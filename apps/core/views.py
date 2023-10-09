

from django.shortcuts import render
from .models import fornecedor


def home(request):
    configuracao = fornecedor.objects.all()

    # Esta verificação é apenas para não deixar o site em branco
    if len(configuracao) > 0:
        configuracao = configuracao[0]
    else:
        configuracao = {
            "slogan": "Slogan",
            "nome_empresa": "Nome da Empresa",
            "telefone": "(00) 00000-0000",
            "email": "email@amil.com"
        }

    dados = {
        "configuracao": configuracao,
    }
    return render(request, "home.html", dados)


