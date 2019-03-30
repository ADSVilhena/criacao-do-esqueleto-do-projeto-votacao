from django.db import models
from django import forms
# Create your models here.
class professor(forms.Form):
    nomeProfessor = forms.CharField(label='nomeProfessor', max_length=100)
    emailProfessor = forms.EmailField(label='emailProfessor', max_length=100)
    senhaProfessor = forms.CharField(label='senhaProfessor', max_length=100)