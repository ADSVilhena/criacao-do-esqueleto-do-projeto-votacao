from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic.base import View

from users.forms import RegUsuarioForm

# Create your views here.
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
            return redirect('login',{'nomeMenu':'Login'})
        else: return redirect('registrar',{'aviso': 'Usuário Existente'} )
        
        return render(request,self.template_name,{'nomeMenu':'Registrar'},{'form':form})

    
