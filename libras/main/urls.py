from django.contrib import admin
from django.urls import path, include
from .views import adicionar_curso, editar_nome_curso,excluir_curso, listar_cursos, n, link


app_name = 'main'


urlpatterns = [
    path('', n, name='main'),
    path('link/<int:cod>', link, name='linkreturn'),
    path('adicionar_curso/', adicionar_curso, name='adicionar_curso'),
    path('excluir_curso/<int:codigo_curso>/', excluir_curso, name='excluir_curso'),
    path('editar_nome_curso/<int:codigo_curso>/', editar_nome_curso, name='editar_nome_curso'),
    path('listar_cursos/', listar_cursos, name='listar_cursos'),
    # Adicione outras URLs conforme necessário
]