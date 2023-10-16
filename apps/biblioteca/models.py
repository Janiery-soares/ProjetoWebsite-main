from django.db import models

class Pizza(models.Model):
    lista_tamanho = [
        ('Família','F'),
        ('Grande','G'),
        ('Média','M'),
        ('pequena','p'),
        ('Brotinho','B'),
    ]
    sabor_pizza = models.CharField(max_length=50, verbose_name='Sabor da Pizza')
    tamamho_pizza = models.CharField(max_length=8, choices=lista_tamanho, verbose_name='Tamanho da Pizza')
    borda_pizza = models.BooleanField(null=True, blank=True, verbose_name='Com Borda')
    descricao_pizza = models.TextField(verbose_name='Descrição da Pizza')
    quantidade_pizza = models.IntegerField(verbose_name='quantidade')
    imagen_produto = models.ImageField(upload_to="foto_pizza/")


    def __str__(self):
        return self.sabor_pizza
    

class Bebida(models.Model):
    nome_bebida = models.CharField(max_length=50)
    ml_bebida = models.IntegerField()
    quantidade_bebida = models.IntegerField()

    def __str__(self):
        return self.nome_bebida
    

