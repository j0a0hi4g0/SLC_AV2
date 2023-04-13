from django.db import models

# Create your models here.

class lista(models.Model):
    nome = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nome}"



class aplicacao(models.Model):
    compra = models.CharField(max_length=64)
    preco = models.IntegerField()
    
    def __str__(self):
        return f"ID:{self.id} Preço:{self.preco}  Produto:{self.compra}"

