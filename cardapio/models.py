from django.db import models

# Create your models here.
class Cardapio(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 255)
    preco = models.DecimalField (max_digits = 5, decimal_places = 2 )