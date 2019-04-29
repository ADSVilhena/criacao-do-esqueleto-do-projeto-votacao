from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Aluno, Votacao, Voto
# Create your views here.

@login_required
def index(request):
    return render(request,'index.html',{'nomeMenu':'Início'})

@login_required
def listarAlunos(request):
    alunos = Aluno.objects.all()
    return render(request,'listar/listarAlunos.html',{'alunos':alunos})

@login_required
def escolherVotacoes(request):
    return render(request,'votacoes/escolherVotacoes.html')

@login_required
def emAndamento(request):
    context = {}
    votacoesEmAndamento = Votacao.objects.filter(estado=1)
    context['votacoesEmAndamento'] = votacoesEmAndamento
    return render(request,'votacoes/emAndamento.html',context)

@login_required
def pausadas(request):
    context = {}
    votacoesPausadas = Votacao.objects.filter(estado=2)
    context['votacoesPausadas'] = votacoesPausadas
    return render(request,'votacoes/pausadas.html',context)
    
@login_required
def concluidas(request):
    context = {}
    votacoesConcluidas = Votacao.objects.filter(estado=3)
    context['votacoesConcluidas'] = votacoesConcluidas
    return render(request,'votacoes/concluidas.html',context)

@login_required
def exibirAluno(request,cpfAluno):
    aluno = Aluno.objects.filter(cpfAluno=cpfAluno)
    votacao = Votacao.objects.filter(aluno=aluno[0])
    context = {}
    context['aluno'] = aluno
    if votacao[0].estado == 1:
        context['template_name'] = 'emAndamento'
    else:
        context['template_name'] = 'finalizada'
    return render(request,'votacoes/exibirAluno.html',context)

@login_required
def voto(request,cpfAluno):
    votacao = Votacao.objects.filter(aluno=Aluno.objects.filter(cpfAluno=cpfAluno))
    escolhas = Voto.escolhas

    return render(request,'votacoes/voto.html',{'escolhas':escolhas})