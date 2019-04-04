from django.shortcuts import render
# Create your views here.
def votacoes(request):
    return render(request,'votacao.html')