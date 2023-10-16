from django.db import models

class Pedido(models.Model):
    adicionar_pedido = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'{self.adicionar_pedido}'
    

class compa(models.Model):
    lista_pagamento = [
        ('Pix','1'),
        ('C.Débito','2'),
        ('C.Crédito','3'),
    ]
    valor_compra = models.DecimalField(max_digits=9, decimal_places=2)
    pagamento_compra = models.CharField(max_length=9, choices=lista_pagamento)

    def __str__(self):
        return self.valor_compra
    