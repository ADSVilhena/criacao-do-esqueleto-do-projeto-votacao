from django.db import models
# Create your models here.
class Usuario(models.Model):
    nomeUsuario = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)