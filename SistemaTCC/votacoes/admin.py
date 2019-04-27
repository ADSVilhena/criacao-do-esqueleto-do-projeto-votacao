from django.contrib import admin
# Register your models here.
from .models import Aluno, Votacao, Voto
admin.site.register(Aluno)
admin.site.register(Votacao)
admin.site.register(Voto)