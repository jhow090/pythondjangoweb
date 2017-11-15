from django.db import models
from django.core.urlresolvers import reverse

class Aluno(models.Model):
    id_aluno = models.CharField(primary_key=True, max_length=10)
    ra_aluno = models.CharField(max_length=10)
    nome_aluno = models.CharField(max_length=100)
    email_aluno = models.CharField(max_length=100)
    celular_aluno = models.CharField(max_length=15)

    def __str__(self):
        return self.id_aluno

class Curso(models.Model):
    id_curso = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nome_curso = models.CharField(max_length=50)
    sigla_curso = models.CharField(max_length=5)

    def __str__(self):
        return self.id_curso
