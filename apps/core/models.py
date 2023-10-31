from django.db import models
from django.contrib.auth.models import User


class DadosCliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    endereço_cliente = models.TextField()
    complemento_cliente = models.TextField()
    telefone_cliente = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=20)
   

    def __str__(self):
        return f"{self.usuario}"
    