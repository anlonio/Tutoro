from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Disciplina(models.Model):
	professores = models.ManyToManyField(User)
	nome = models.CharField(max_length=50)
	sigla = models.CharField(max_length=10)

class Instituicao(models.Model):
	professsor = models.ManyToManyField(User)
	nome = models.CharField(max_length=150)
	cidade = models.CharField(max_length=100)
	uf = models.CharField(max_length=2)
	sigla = models.CharField(max_length=10)
	descricao = models.TextField(max_length=255)

class Duvida(models.Model):
	titulo = models.CharField(max_length=250)
	texto = models.TextField(max_length=1000)
	imagem = models.ImageField(upload_to='duvida/%Y/%m/%d/')
	audio = models.FileField(upload_to='duvida/%Y/%m/%d/')
	video = models.FileField(upload_to='duvida/%Y/%m/%d/')
	like = models.ManyToManyField(User)
	deslike = models.ManyToManyField(User)
	disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL , null=True)
