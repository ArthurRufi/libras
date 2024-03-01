from django.db import models

class Cursos(models.Model):
    nome = models.CharField(max_length=200)
    codigocurso = models.IntegerField()

    @classmethod
    def adicionar_curso(cls, nome, codigo):
        novo_curso = cls(nome=nome, codigocurso=codigo)
        novo_curso.save()

    @classmethod
    def excluir_curso(cls, codigo):
        cls.objects.filter(codigocurso=codigo).delete()

    @classmethod
    def editar_nome_curso(self, novo_nome):
        self.nome = novo_nome
        self.save()

    def __str__(self):
        return f'{self.nome}'
    
        

class VideosCurso(models.Model):
    codigocurso = models.IntegerField()
    link = models.CharField(max_length=200)

    @classmethod
    def editar_video_curso(cls, codigo_curso, novo_link):
        video_curso = cls.objects.get(codigocurso=codigo_curso)
        video_curso.link = novo_link
        video_curso.save()

    @classmethod
    def adicionar_video_curso(cls, codigo_curso, link):
        novo_video = cls(codigocurso=codigo_curso, link=link)
        novo_video.save()

    def __str__(self):
        return f'{self.nome}'