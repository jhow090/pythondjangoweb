from django.db import models
from django.core.urlresolvers import reverse

class Aluno(models.Model):
    ra_aluno = models.CharField(max_length=10)
    nome_aluno = models.CharField(max_length=100)
    email_aluno = models.CharField(max_length=100)
    celular_aluno = models.CharField(max_length=15)
    curso_aluno = models.CharField(max_length=50)

class Curso(models.Model):
    nome_curso = models.CharField(max_length=50)
    sigla_curso = models.CharField(max_length=5)


class Professor(models.Model):
    ra_professor = models.CharField(max_length=10)
    apelido_professor = models.CharField(max_length=30)
    nome_professor = models.CharField(max_length=120)
    email_professor = models.CharField(max_length=80)
    celular_professor = models.CharField(max_length=11)

class Matricula(models.Model):
    ra_aluno_matricula = models.CharField(max_length=10)
    nome_disciplina_matricula = models.CharField(max_length=200)
    ano_ofertado_matricula = models.CharField(max_length=10)
    semestre_ofertado_matricula = models.CharField(max_length=10)
    id_turma_matricula  = models.CharField(max_length=10)

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    data_nascimento = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=10)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=15)
