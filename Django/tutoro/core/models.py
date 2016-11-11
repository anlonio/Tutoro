from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Asssunto(models.Model):
	nome = models.CharField(max_length=50)

	def __str__(self):
		return self.nome


class Disciplina(models.Model):
	professores = models.ManyToManyField(User, blank=True)
	nome = models.CharField(max_length=50)
	sigla = models.CharField(max_length=10, unique=True)

	def __str__(self):
		return self.nome


class Instituicao(models.Model):
	admin = models.ForeignKey(User)
	professsores = models.ManyToManyField(User, related_name='professsores', blank=True)
	alunos = models.ManyToManyField(User, related_name='alunos', blank=True)
	nome = models.CharField(max_length=150)
	cidade = models.CharField(max_length=100)
	uf = models.CharField(max_length=2)
	sigla = models.CharField(max_length=10)
	descricao = models.TextField(max_length=255, blank=True)

	def __str__(self):
		return self.nome + ", " + self.cidade + "/" + self.uf

class Duvida(models.Model):
	autor = models.ForeignKey(User)
	titulo = models.CharField(max_length=250)
	texto = models.TextField(max_length=1000, blank=True)
	imagem = models.ImageField(upload_to='duvida/imagens/%Y/%m/%d/', blank=True, null=True)
	audio = models.FileField(upload_to='duvida/audios/%Y/%m/%d/', blank=True, null=True)
	video = models.FileField(upload_to='duvida/videos/%Y/%m/%d/', blank=True, null=True)
	like = models.ManyToManyField(User, related_name='like_question', blank=True)
	deslike = models.ManyToManyField(User, related_name='deslike_question', blank=True)
	disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL , null=True)
	assuntos = models.ManyToManyField(Asssunto, related_name='assuntos', \
		blank=True)
	respondida = models.BooleanField(default=False)
	date_create = models.DateTimeField(default=timezone.now)
	last_update = models.DateTimeField(blank=True, null=True)

	def save(self):
		self.last_update = timezone.now()
		super(Duvida, self).save()

	def __str__(self):
		return self.date_create.strftime("[%d/%m/%Y] ") + self.autor.username + ": " + self.titulo[:40] + "..."

class Comentario(models.Model):
	duvida = models.ForeignKey(Duvida)
	autor = models.ForeignKey(User)
	texto = models.TextField(max_length=1000, blank=True)
	imagem = models.ImageField(upload_to='comentario/imagens/%Y/%m/%d/', blank=True, null=True)
	audio = models.FileField(upload_to='comentario/audios/%Y/%m/%d/', blank=True, null=True)
	video = models.FileField(upload_to='comentario/videos/%Y/%m/%d/', blank=True, null=True)
	like = models.ManyToManyField(User, related_name='like_comment', blank=True)
	deslike = models.ManyToManyField(User, related_name='deslike_comment', blank=True)
	date_create = models.DateTimeField(default=timezone.now)
	last_update = models.DateTimeField(blank=True, null=True)

	def save(self):
		self.last_update = timezone.now()
		super(Comentario, self).save()

	def __str__(self):
		return self.date_create.strftime("[%d/%m/%Y] ") + self.autor.username + ": " + self.texto[:40] + "..."
