from django.db import models

from apps.vendas.models import (Compra)

class Pizza(models.Model):
    lista_tamanho = [
        ('F','Família'),
        ('G','Grande'),
        ('M','Média'),
        ('p','pequena'),
        ('B','Brotinho'),
    ]
    sabor_pizza = models.CharField(max_length=50, verbose_name='Sabor da Pizza')
    tamamho_pizza = models.CharField(max_length=8, choices=lista_tamanho, verbose_name='Tamanho da Pizza')
    descricao_pizza = models.TextField(verbose_name='Descrição da Pizza')
    quantidade_pizza = models.IntegerField(verbose_name='quantidade')
    valor_compra = models.OneToOneField(Compra, on_delete=models.CASCADE)
    imagem_pizza = models.ImageField(upload_to="/midia/foto_pizza")


    def __str__(self):
        return self.sabor_pizza
    

class Bebida(models.Model):
    nome_bebida = models.CharField(max_length=50)
    ml_bebida = models.IntegerField()
    quantidade_bebida = models.IntegerField()
    valor_compra = models.OneToOneField(Compra, on_delete=models.CASCADE)
    imagem_refri = models.ImageField(upload_to="/midia/foto_refri")

    def __str__(self):
        return self.nome_bebida
    

