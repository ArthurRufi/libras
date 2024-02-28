from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Cursos, VideosCurso
from apicursos.models import SinalsArchives


def n(request):
    na= Cursos.objects.values('nome', 'codigocurso')
    return render(request, 'main/html/index.html', {'nome': na})


def link(request, cod):
    try:
        redirection = VideosCurso.objects.get(codigocurso = cod)
        codigo = cod
        cursoname = Cursos.objects.get(codigocurso = cod)
        link_do_video = redirection.link
        sinal = SinalsArchives.objects.values('nome', 'descricaolibras', 'descricaolibras', 'linkvideo', 'imagem', 'codigocurso')
        
        
        return render(request, 'main/html/anjo.html', {'link_do_video': link_do_video, 'nome': cursoname, 'sinal': sinal, 'codigo': codigo})
    
    except redirection.DoesNotExist:
        return HttpResponse('INNASNDN')


def sinais(request, curso, sinal):
    try:
        redirection = SinalsArchives.objects.all()
        return render(request, 'main/html/details.html')
    except redirection.DoesNotExist:
        return HttpResponse('agua mineral')


def tutotial(request):
   return HttpResponse ('aui')