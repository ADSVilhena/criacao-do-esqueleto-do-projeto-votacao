from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic.base import View

from users.forms import RegUsuarioForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')

class registrarUsuarioView(View):
    template_name = 'registrar.html'
    
    def get(self,request):
        return render(request,self.template_name,{'nomeMenu':'Registrar'})
    
    def post(self,request):
        form = RegUsuarioForm(request.POST)

        if form.valido:
            dadosForm = form.data
            novoUsuario = User.objects.create_user(dadosForm['nome'],dadosForm['email'],dadosForm['senha'])
            novoUsuario.save()
            return redirect('login')
        
        return render(request,self.template_name,{'nomeMenu':'Registrar'},{'form':form})

    
