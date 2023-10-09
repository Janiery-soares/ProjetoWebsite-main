from django.db import models
from apps.biblioteca.models import *


class DadosCliente(models.Model):
    nome_cliente = models.CharField(max_length=100)
    endereço_cliente = models.TextField()
    complemento_cliente = models.TextField()
    telefone_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_cliente
    

class DadosPessoais(models.Model):
        cpf = models.CharField(max_length=14)
        rg = models.CharField(max_length=10)
        dadoscliente = models.OneToOneField(DadosCliente, on_delete=models.CASCADE)


        def __str__(self):
             return self.cpf
        