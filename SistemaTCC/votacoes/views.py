from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Aluno, Votacao
# Create your views here.

@login_required
def index(request):
    return render(request,'index.html',{'nomeMenu':'Início'})
@login_required
def listarAlunos(request):
    alunos = Aluno.objects.all()
    return render(request,'listar/listarAlunos.html',{'alunos':alunos})
@login_required
def emAndamento(request):
    emAdamento = Votacao.objects.all()
    print('aaaaaaaaaaaa', emAndamento)
    return render(request,'votacoes/emAndamento.html',{'listaEmAndamento':emAndamento})
@login_required
def concluidas(request):
    concluidas = Votacao.objects.filter(concluida=True)
    return render(request,'votacoes/concluidas.html',{'listaConcluidas':concluidas})
