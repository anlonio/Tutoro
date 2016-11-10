from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Disciplina(models.Model):
	professores = models.ManyToManyField(User)
	nome = models.CharField(max_length=50)
	sigla = models.CharField(max_length=10)