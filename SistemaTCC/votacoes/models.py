from django.db import models
from django import forms
# Create your models here.
class Aluno(models.Model):

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

    salaAluno = models.CharField(    
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
 
    objetos = models.Manager() 

