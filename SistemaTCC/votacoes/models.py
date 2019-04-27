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
    def __str__(self):
        return self.nomeAluno

class Votacao(models.Model):
    aluno = models.ForeignKey(Aluno,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now, editable=False)
    emAndamento = 1
    pausada = 2
    finalizada = 3
    escolhas =(
        (1,'Em Andamento'),
        (2,'Pausada'),
        (3,'Finalizada')
    )
    estado = models.IntegerField(choices=escolhas, default=2)

    def __str__(self):
        return self.aluno.nomeAluno

class Voto(models.Model):
    sim = 1
    nao = 2
    abstencao = 3
    escolhas =(
        (1,'Sim'),
        (2,'Não'),
        (3,'Abstenção')
    )
    voto = models.IntegerField(choices=escolhas,default=3)
    professor = models.ForeignKey(User,on_delete=models.CASCADE)
    votacao = models.ForeignKey(Votacao,on_delete=models.CASCADE)

    def __str__(self):
        return 'Professor: '+ self.professor.username