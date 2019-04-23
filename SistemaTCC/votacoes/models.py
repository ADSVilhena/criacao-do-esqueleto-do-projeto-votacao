from django.db import models
from django import forms
from django.utils.timezone import now

# Create your models here.
class Aluno(models.Model):
    imagemAluno = models.ImageField(upload_to='images/alunos')
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

class Votacao(models.Model):
    aluno = models.ForeignKey(Aluno,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now, editable=False)
    votosP = models.IntegerField(default=0)
    votosN = models.IntegerField(default=0)
    concluida = models.BooleanField(default=False)