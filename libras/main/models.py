from django.db import models

# Create your models here.
class Cursos(models.Model):
    nome = models.CharField(max_length=200) 
    logocurso = models.BinaryField()#adicionar aqui o local do upload, sair do binario
    descricao = models.CharField(max_length=400)