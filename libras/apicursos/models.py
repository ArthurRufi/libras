from django.db import models

# Create your models here.

class SinalsArchives(models.Model):
    
    nome = models.CharField (max_length =255)
    imagem = models.IntegerField()
    linkvideo = models.CharField(max_length = 1000)
    descricaoptbr = models.CharField(max_length = 2000)
    descricaolibras = models.CharField(max_length= 1000)
    codigosinal = models.IntegerField(default=404)
    codigocurso = models.IntegerField(default=404)
    codigodamateria = models.IntegerField(default = 0)
    linkqrcode = models.TextField(default='lll')
    def __str__(self):
        return f'{self.nome}'


class Materia(models.Model):

    nomemateria = models.CharField(max_length = 1000)
    codigomateria = models.IntegerField()
    codigocurso = models.IntegerField()
    def __str__(self):
        return f'{self.nomemateria}'