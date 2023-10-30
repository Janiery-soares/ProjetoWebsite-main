from django.db import models
from apps.produtos.models import (Pizza)
from apps.produtos.models import (Bebida)

class Pedido(models.Model):
    adicionar_pedido = models.BooleanField(null=True, blank=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE )
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.adicionar_pedido}'
    

class Compra(models.Model):
    lista_pagamento = [
        ('Pix','Pix'),
        ('C.Débito','C.Débito'),
        ('C.Crédito','C.Crédito'),
    ]
    valor_compra = models.DecimalField(max_digits=9, decimal_places=2)
    pagamento_compra = models.CharField(max_length=9, choices=lista_pagamento)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.valor_compra}'
    