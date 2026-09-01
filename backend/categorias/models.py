from django.db import models

# Create your models here.

class Categoria(models.Model):
    TIPO_CHOICES = [
        ('RECEITA','Receita'),
        ('DESPESA','Despesa'),
]
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.nome} ({self.tipo})"