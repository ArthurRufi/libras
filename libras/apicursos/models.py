from django.db import models

# Create your models here.
class SinalsArchives(models.Model):
    
    nome = models.CharField (max_length =255)
    imagem = models.IntegerField()
    linkvideo = models.CharField(max_length = 1000)
    descricaoptbr = models.CharField(max_length = 2000)
    descricaolibras = models.CharField(max_length= 1000)