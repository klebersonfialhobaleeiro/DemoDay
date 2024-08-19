from django.db import models
from produtos.models import Produto

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.produto} - {self.quantidade} unidades em estoque"
