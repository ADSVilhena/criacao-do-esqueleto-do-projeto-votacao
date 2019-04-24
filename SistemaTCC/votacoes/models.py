from django.db import models
from django import forms
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
class Aluno(models.Model):
    imagemAluno = models.ImageField(upload_to='images/')
    nomeAluno = models.CharField(
        max_length=255,    
        null=False,     
        blank=False   
    ) 
    cursoAluno = models.CharField(    
        max_length=50,     
        null=False,     
        blank=False   
    ) 
    turmaAluno = models.CharField(    
        max_length=1,     
        null=False,     
        blank=False   
    ) 
    cpfAluno = models.CharField(    
        max_length=14,     
        null=False,     
        blank=False   
    ) 
    serieAluno = models.IntegerField(    
        null=False,     
        blank=False,
    )
class Voto(models.Model):
    voto = models.IntegerField(default=0)
    user = models.CharField(default="Vazio", max_length=255)

class Votacao(models.Model):
    aluno = models.ForeignKey(Aluno,on_delete=models.CASCADE)
    #voto = models.ForeignKey(Voto,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now, editable=False)
    concluida = models.BooleanField(default=False)    