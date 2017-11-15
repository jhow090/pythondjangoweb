from django.db import models
from django.core.urlresolvers import reverse

class Aluno(models.Model):
    id_aluno = models.CharField(primary_key=True, max_length=10)
    ra_aluno = models.CharField(max_length=10)
    nome_aluno = models.CharField(max_length=100)
    email_aluno = models.CharField(max_length=100)
    celular_aluno = models.CharField(max_length=15)

class Curso(models.Model):
    id_curso = models.CharField(primary_key=True, max_length=10)
    nome_curso = models.CharField(max_length=50)
    sigla_curso = models.CharField(max_length=5)

class Disciplina(models.Model):
    id_disciplina = models.CharField(primary_key=True, max_length=10)
    nome_disciplina = models.CharField(max_length=240)
    carga_horaria_disciplina = models.CharField(max_length=100)
    teoria_disciplina = models.CharField(max_length=100)
    pratica_disciplina = models.CharField(max_length=100)
    ementa_disciplina = models.CharField(max_length=50)
    competencias_disciplina = models.CharField(max_length=50)
    habilidades_disciplina = models.CharField(max_length=50)
    conteudo_disciplina = models.CharField(max_length=50)
    bibliografia_disciplina = models.CharField(max_length=50)
    bibliografia_complementar_disciplina = models.CharField(max_length=50)
