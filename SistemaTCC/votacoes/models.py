from django.db import models
from django import forms
from django.utils.timezone import now
from django.contrib.auth.models import User


class Aluno(models.Model):
    imagemAluno = models.ImageField(upload_to='images/')
    nomeAluno = models.CharField(
        max_length=255,    
        null=False,     
        blank=False   
    ) 
    cpfAluno = models.CharField(    
        max_length=14,     
        null=False,     
        blank=False   
    )
    turmaAluno = models.ForeignKey("Turma",on_delete=models.CASCADE)
    def __str__(self):
        return self.nomeAluno

class Curso(models.Model):
    curso = models.CharField(max_length=15, null=False,blank=False) 
    def __str__(self):
        return self.curso
    
class Ano(models.Model):
    ano = models.CharField(max_length=1, null=False,blank=False) 
    def __str__(self):
        return self.ano+"º "

class Turma(models.Model):
    nomeTurma = models.CharField(max_length=1, null=False,blank=False) 
    anoTurma = models.ForeignKey(Ano,on_delete=models.CASCADE)
    cursoTurma = models.ForeignKey(Curso,on_delete=models.CASCADE)
    def __str__(self):
        return self.cursoTurma.curso+": " + self.anoTurma.ano +"º "+ self.nomeTurma

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
    class Meta:
        verbose_name_plural = 'votações'


class Voto(models.Model):
    VOTO_SIM = 1
    VOTO_NAO = 2
    VOTO_ABSTENCAO = 3
    escolhas =(
        (1,'Sim'),
        (2,'Não'),
        (3,'Abstenção')
    )
    voto = models.IntegerField(choices=escolhas,default=VOTO_ABSTENCAO)
    professor = models.ForeignKey(User,on_delete=models.CASCADE)
    votacao = models.ForeignKey(Votacao,on_delete=models.CASCADE)

    def __str__(self):
        return 'Professor: "'+ self.professor.username + '"  Votacao: "'+self.votacao.aluno.nomeAluno + '"'