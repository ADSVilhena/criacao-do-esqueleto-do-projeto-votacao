from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Aluno, Votacao, Voto
from .forms import votoForm

@login_required
def index(request):
    nomeUsuario = request.user.username
    context = {}
    context['nomeUsuario'] = nomeUsuario
    context['nomeMenu'] = 'Início'
    return render(request,'index.html',context)

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
    aluno = Aluno.objects.get(cpfAluno=cpfAluno)
    votacao = Votacao.objects.get(aluno=aluno)
    context = {}
    context['aluno'] = aluno
    context['votacao'] = votacao
    context['professor'] = request.user
    context['form'] = votoForm

    professoresVotaram = []
    votos = Voto.objects.filter(votacao = votacao)
    for v in votos:
        professoresVotaram.append(v.professor)
    context['votaram'] = professoresVotaram
    

    if votacao.estado == 1:
        context['template_name'] = 'emAndamento'
    else:
        context['template_name'] = 'finalizada'

    if request.method == 'POST': 
        form = votoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect("exibirAluno",cpfAluno = cpfAluno)
        else:
            print(form.errors)
    else:
        form = votoForm()
    return render(request,'votacoes/exibirAluno.html',context)