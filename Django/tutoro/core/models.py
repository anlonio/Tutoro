from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Disciplina(models.Model):
	professores = models.ManyToManyField(User)
	nome = models.CharField(max_length=50)
	sigla = models.CharField(max_length=10)

class Instituicao(models.Model):
	professsor = models.ManyToMany(User)
	nome = models.CharField(max_length=150)
	cidade = models.CharField(max_length=100)
	uf = models.CharField(max_length=2, min_length=4)
	sigla = models.CharField(max_length=10, min_length=2)
	descricao = models.TextField(max_length=255)