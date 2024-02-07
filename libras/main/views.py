from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Cursos, VideosCurso


def n(request):
    return render(request, 'main/html/index.html')


def adicionar_curso(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        codigo = int(request.POST.get('codigo'))

        Cursos.adicionar_curso(nome=nome, codigo=codigo) 
        return HttpResponse("Curso adicionado com sucesso!")

    return render(request, 'sua_template.html')  # Substitua 'sua_template.html' pelo nome do seu template


def excluir_curso(request, codigo_curso):
    Cursos.excluir_curso(codigo=codigo_curso)
    return HttpResponse("Curso excluído com sucesso!")


def editar_nome_curso(request, codigo_curso):
    if request.method == 'POST':
        novo_nome = request.POST.get('novo_nome')

        curso = get_object_or_404(Cursos, codigocurso=codigo_curso)
        curso.editar_nome_curso(novo_nome=novo_nome)

        return HttpResponse("Nome do curso editado com sucesso!")

    return render(request, 'sua_template.html')  # Substitua 'sua_template.html' pelo nome do seu template

def listar_cursos(request):
    cursos = Cursos.objects.all()
    return render(request, 'listar_cursos.html', {'cursos': cursos})
