from django.db import models

class Fornecedor(models.Model):
    nome_fornecedor = models.CharField(max_length=100)
    endereço_fornecedor = models.TextField()
    telefone_fornecedor = models.CharField(max_length=100)
    email_fornecedor = models.EmailField()

    def __str__(self):
        return self.nome_fornecedor


class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    quantidade_produto = models.IntegerField()
    descricao_produto = models.TextField
    validade_produto = models.DateField(null=True, blank=True)
    codigo_produto = models.IntegerField()

    def __str__(self):
        return self.nome_produto
    