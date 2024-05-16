from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from .models import Cursos, VideosCurso
from apicursos.models import SinalsArchives, Materia
from .static.main.utils.qrcode import qrcodegenerator

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
    linknow = request.get_full_path()
    ipnick = "http://192.168.0.12:8000" + linknow
    qrcodegenerator(ipnick)
    print(ipnick)
    signallink = sinal
    cursolink = curso
    try:
        redirection = SinalsArchives.objects.values('nome', 'descricaolibras', 'descricaolibras', 'linkvideo', 'imagem', 'codigocurso', 'codigodamateria')
        sinalref = SinalsArchives.objects.get(codigosinal = sinal)
        return render(request, 'main/html/details.html', {'nome': sinalref.nome, 'descricaolibras': sinalref.descricaolibras, 'descricao': sinalref.descricaoptbr,
                                                           'linkvideo': sinalref, 'imagem': sinalref.imagem, 'codigocurso': sinalref.codigocurso,
                                                            'codigodamateria': sinalref.codigodamateria, 'qrcode': sinalref.linkqrcode, 'linksinal': signallink, 'cursolink': cursolink})
        
    except (redirection.DoesNotExist):
        return HttpResponse('agua mineral')
    


def tutotial(request):
   return HttpResponse ('aui')


def opcaodetails(request, curso, sinal, opcao):
    linknow = request.get_full_path()
    ipnick = "http://192.168.0.12:8000" + linknow
    qrcodegenerator(ipnick)
    print(ipnick)
    select_option = opcao
    signallink = sinal
    cursolink = curso
    try:
        redirection = SinalsArchives.objects.values('nome', 'descricaolibras', 'descricaolibras', 'linkvideo', 'imagem', 'codigocurso', 'codigodamateria')
        sinalref = SinalsArchives.objects.get(codigosinal = sinal)
        return render(request, 'main/html/opcaodetails.html', {'nome': sinalref.nome, 'descricaolibras': sinalref.descricaolibras, 'descricao': sinalref.descricaoptbr,
                                                           'linkvideo': sinalref, 'imagem': sinalref.imagem, 'codigocurso': sinalref.codigocurso,
                                                            'codigodamateria': sinalref.codigodamateria, 'qrcode': sinalref.linkqrcode, 'opcao' : select_option,
                                                            'linksinal': signallink, 'cursolink': cursolink})
        
    except SinalsArchives.DoesNotExist:
        # Se o objeto não for encontrado, levanta uma exceção Http404
        raise Http404('A página que você está procurando não existe.')