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

