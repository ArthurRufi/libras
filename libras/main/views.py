from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Cursos, VideosCurso


def n(request):
    na= Cursos.objects.values('nome', 'codigocurso')
    return render(request, 'main/html/index.html', {'nome': na})


def link(request, cod):
    try:
        redirection = VideosCurso.objects.get(codigocurso = cod)
        cursoname = Cursos.objects.get(codigocurso = cod)
        link_do_video = redirection.link  
        return render(request, 'main/html/anjo.html', {'link_do_video': link_do_video, 'nome': cursoname})
    
    except redirection.DoesNotExist:
        return HttpResponse('INNASNDN')

def adicionar_curso(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        codigo = int(request.POST.get('codigo'))

        Cursos.adicionar_curso(nome=nome, codigo=codigo) 
        return HttpResponse("Curso adicionado com sucesso!")

    return render(request, 'sua_template.html')  


def excluir_curso(request, codigo_curso):
    Cursos.excluir_curso(codigo=codigo_curso)
    return HttpResponse("Curso excluído com sucesso!")


def editar_nome_curso(request, codigo_curso):
    if request.method == 'POST':
        novo_nome = request.POST.get('novo_nome')

        curso = get_object_or_404(Cursos, codigocurso=codigo_curso)
        curso.editar_nome_curso(novo_nome=novo_nome)

        return HttpResponse("Nome do curso editado com sucesso!")

    return render(request, 'sua_template.html') 

def listar_cursos(request):
    cursos = Cursos.objects.all()
    return render(request, 'listar_cursos.html', {'cursos': cursos})
