from django.shortcuts import render
# Create your views here.
def registrar(request):
    return render(request,'registrar.html')
    
def votacoes(request):
    return render(request,'votacao.html')
    
def login(request):
    return render(request,'login.html')

def index (request):
    return render(request,'index.html')

