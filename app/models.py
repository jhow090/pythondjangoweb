from django.db import models
from django.core.urlresolvers import reverse

class Aluno(models.Model):
    ra_aluno = models.CharField(max_length=10)
    nome_aluno = models.CharField(max_length=100)
    email_aluno = models.CharField(max_length=50)
    celular_aluno = models.CharField(max_length=15)
    sigla_curso = models.CharField(max_length=5)

class Curso(models.Model):
    nome_curso = models.CharField(max_length=50)
    sigla_curso = models.CharField(max_length=5)

class Disciplina(models.Model):
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

class Disciplinofertada(models.Model):
    nome_disciplina = models.CharField(max_length=240)
    ano_disciplina = models.CharField(max_length=5)
    semestre_disciplina = models.CharField(max_length=5)

class Grade(models.Model):
    sigla_curso = models.CharField(max_length=5)
    ano_grade = models.CharField(max_length=5)
    semestre_grade = models.CharField(max_length=5)

class Matricula(models.Model):
    ra_aluno = models.CharField(max_length=5)
    nome_disciplina = models.CharField(max_length=240)
    ano_disciplina = models.CharField(max_length=5)
    semestre_disciplina = models.CharField(max_length=5)
    id_turma = models.CharField(max_length=5)

class Periodo(models.Model):
    sigla_curso = models.CharField(max_length=5)
    ano_grade = models.CharField(max_length=5)
    semestre_grade = models.CharField(max_length=5)
    numero_periodo = models.CharField(max_length=5)

class Perioddisciplina(models.Model):
    sigla_curso = models.CharField(max_length=5)
    ano_grade = models.CharField(max_length=5)
    semestre_grade = models.CharField(max_length=5)
    numero_periodo = models.CharField(max_length=5)
    nome_disciplina = models.CharField(max_length=240)

class Professor(models.Model):
    ra_professor = models.CharField(max_length=10)
    apelido_professor = models.CharField(max_length=30)
    nome_professor = models.CharField(max_length=120)
    email_professor = models.CharField(max_length=80)
    celular_professor = models.CharField(max_length=11)

class Turma(models.Model):
    nome_disciplina = models.CharField(max_length=240)
    ano_disciplina = models.CharField(max_length=5)
    semestre_disciplina = models.CharField(max_length=5)
    turno_turma = models.CharField(max_length=15)
    ra_professor = models.CharField(max_length=11)
