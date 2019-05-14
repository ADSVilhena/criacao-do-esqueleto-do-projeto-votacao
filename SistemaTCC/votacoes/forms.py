from django import forms
from django.contrib.auth.models import User
from .models import Voto

class votoForm(forms.ModelForm):
    class Meta:
        model = Voto
        fields = ['voto','professor','votacao']
        widgets={'voto':forms.RadioSelect()}