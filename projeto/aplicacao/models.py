from django.db import models


class Lista(models.Model):
    nome = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nome}"

class Aplicacao(models.Model):
    compra = models.CharField(max_length=64)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"ID:{self.id} Preço:{self.preco}  Produto:{self.compra}"



class ListaCompras(models.Model):
    nome = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.quantidade} - {self.item} - R$ {self.valor}'

    def total(self):
        return self.quantidade * self.valor

    total.short_description = 'total'
