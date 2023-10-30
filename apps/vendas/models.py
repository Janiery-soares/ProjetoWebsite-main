from django.db import models
from .models import *
from apps.produtos.models import Pizza
from apps.produtos.models import Bebida
from apps.core.models import User


class Pedido(models.Model):

    lista_pagamento = [
        ('1','Pix'),
        ('2','C.Débito'),
        ('3','C.Crédito'),
    ]
      
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE )
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)
    valor_compra = models.DecimalField(max_digits=9, decimal_places=2)
    pagamento_compra = models.CharField(max_length=9, choices=lista_pagamento)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    

def __str__(self):
    return f'{self.valor_compra}'
    