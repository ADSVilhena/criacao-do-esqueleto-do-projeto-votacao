from django import forms
from django.contrib.auth.models import User

class RegUsuarioForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)
     
    def valido(self):
        valido = True

        if not super(RegUsuarioForm,self).valido:
            valido=False
        
        usuarioExistente=User.objects.filter(username=self.data['email']).exists()
        if usuarioExistente:
            valido=False

        return valido
            