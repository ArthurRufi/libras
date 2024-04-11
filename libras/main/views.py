from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Cursos, VideosCurso
from apicursos.models import SinalsArchives, Materia


def n(request):
    na= Cursos.objects.values('nome', 'codigocurso')
    return render(request, 'main/html/index.html', {'nome': na})


def link(request, cod):
    try:
        redirection = VideosCurso.objects.get(codigocurso = cod)
        codigo = cod
        cursoname = Cursos.objects.get(codigocurso = cod)
        link_do_video = redirection.link
        sinal = SinalsArchives.objects.values('nome', 'descricaolibras', 'descricaolibras', 'linkvideo', 'imagem', 'codigocurso', 'codigodamateria')
        materias = Materia.objects.values('nomemateria', 'codigomateria', 'codigocurso')
        
        
        return render(request, 'main/html/anjo.html', {'link_do_video': link_do_video, 'nome': cursoname, 'sinal': sinal, 'codigo': codigo, 'materia': materias,})
    
    except (redirection.DoesNotExist, UnboundLocalError):
        return HttpResponse('INNASNDN')


def sinais(request, curso, sinal):
    try:
        redirection = SinalsArchives.objects.values('nome', 'descricaolibras', 'descricaolibras', 'linkvideo', 'imagem', 'codigocurso', 'codigodamateria')
        sinalref = SinalsArchives.objects.get(codigosinal = sinal)
        return render(request, 'main/html/details.html', {'nome': sinalref.nome, 'descricaolibras': sinalref.descricaolibras, 'descricao': sinalref.descricaoptbr,
                                                           'linkvideo': sinalref, 'imagem': sinalref.imagem, 'codigocurso': sinalref.codigocurso,
                                                            'codigodamateria': sinalref.codigodamateria})
        
    except (redirection.DoesNotExist):
        return HttpResponse('agua mineral')
    


def tutotial(request):
   return HttpResponse ('aui')