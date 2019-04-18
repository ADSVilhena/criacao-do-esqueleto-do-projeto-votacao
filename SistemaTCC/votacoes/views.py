from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    return render(request,'index.html',{'nomeMenu':'Início'})
@login_required
def cadastroAluno(request): 
    return render(request,'cadastros/cadAluno.html',{'nomeMenu':'Cadastrar Aluno'})