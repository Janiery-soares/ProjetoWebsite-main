from django.db import models
from apps.vendas.models import *
from django.contrib.auth.models import User


class DadosCliente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    endereço_cliente = models.TextField()
    complemento_cliente = models.TextField()
    telefone_cliente = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=10)
    compra = models.OneToOneField(Compra, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.usuario   