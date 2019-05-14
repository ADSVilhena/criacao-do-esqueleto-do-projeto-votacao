from django.contrib import admin
# Register your models here.
from .models import Aluno, Votacao, Voto, Curso,Turma,Ano
admin.site.register(Aluno)
admin.site.register(Votacao)
admin.site.register(Voto)
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Ano)