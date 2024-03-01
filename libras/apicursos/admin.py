from django.contrib import admin
from main.models import Cursos, VideosCurso
from .models import SinalsArchives, Materia
# Register your models here.

admin.site.register(Cursos)
admin.site.register(VideosCurso)
admin.site.register(SinalsArchives)
admin.site.register(Materia)

