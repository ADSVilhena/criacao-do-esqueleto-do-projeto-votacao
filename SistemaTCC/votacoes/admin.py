from django.contrib import admin
# Register your models here.
from .models import Aluno, Votacao
admin.site.register(Aluno)
admin.site.register(Votacao)