from django import forms
from django.forms import ModelForm
from models import *
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class AlunoForm(forms.ModelForm):
        ra_aluno = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'title': 'Ra',
                'type': 'number',
                'name': 'ra_aluno',
                'id': 'ra_aluno',
                'size': 10,
                'placeholder': 'Ra'
            }
        )
    )
        nome_aluno = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'title': 'Nome',
                'type': 'text',
                'name': 'nome_aluno',
                'id': 'nome_aluno',
                'size': 15,
                'placeholder': 'Nome'
            }
        )
    )

        email_aluno = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'title': 'Email',
                'type': 'email',
                'name': 'email_aluno',
                'id': 'email_aluno',
                'size': 15,
                'placeholder': 'Email'
            }
        )
    )

        celular_aluno = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'title': 'Celular',
                'type': 'number',
                'name': 'celular_aluno',
                'id': 'celular_aluno',
                'size': 10,
                'placeholder': 'Celular'
            }
        )
    )


        class Meta:
            model = Aluno
            fields =    ['ra_aluno',
                        'nome_aluno',
                        'email_aluno',
                        'celular_aluno',
                        'sigla_curso']


class CursoForm(forms.ModelForm):
        nome_curso = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'title': 'Nome',
                'type': 'text',
                'name': 'nome_curso',
                'id': 'nome_curso',
                'size': 15,
                'placeholder': 'Nome'
            }
        )
    )
        sigla_curso = forms.CharField(
        max_length=3,
        widget=forms.TextInput(
            attrs={
                'title': 'Sigla',
                'type': 'text',
                'name': 'sigla_curso',
                'id': 'sigla_curso',
                'size': 5,
                'placeholder': 'Sigla'
            }
        )
    )

        class Meta:
            model = Curso
            fields =    ['nome_curso',
                        'sigla_curso']

class DisciplinaForm(forms.ModelForm):
        nome_disciplina = forms.CharField(
        max_length=240,
        widget=forms.TextInput(
            attrs={
                'title': 'Nome da disciplina',
                'type': 'text',
                'name': 'nome_disciplina',
                'id': 'nome_disciplina',
                'size': 15,
                'placeholder': 'Nome da disciplina'
            }
        )
    )
        carga_horaria_disciplina = forms.CharField(
        max_length=3,
        widget=forms.TextInput(
            attrs={
                'title': 'Carga horaria',
                'type': 'text',
                'name': 'carga_horaria_disciplina',
                'id': 'carga_horaria_disciplina',
                'size': 10,
                'placeholder': 'Carga horaria'
            }
        )
    )

        teoria_disciplina = forms.CharField(
        max_length=3,
        widget=forms.TextInput(
            attrs={
                'title': 'Teoria',
                'type': 'text',
                'name': 'teoria_disciplina',
                'id': 'teoria_disciplina',
                'size': 5,
                'placeholder': 'Teoria'
            }
        )
    )

        pratica_disciplina = forms.CharField(
        max_length=3,
        widget=forms.TextInput(
            attrs={
                'title': 'Pratica',
                'type': 'text',
                'name': 'pratica_disciplina',
                'id': 'pratica_disciplina',
                'size': 5,
                'placeholder': 'Pratica'
            }
        )
    )

        ementa_disciplina = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'title': 'Ementa',
                'type': 'text',
                'name': 'ementa_disciplina',
                'id': 'ementa_disciplina',
                'size': 15,
                'placeholder': 'Ementa'
            }
        )
    )

        competencias_disciplina = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'title': 'Competencias',
                'type': 'text',
                'name': 'competencias_disciplina',
                'id': 'competencias_disciplina',
                'size': 15,
                'placeholder': 'Competencias'
            }
        )
    )
        habilidades_disciplina = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'title': 'Habilidades',
                'type': 'text',
                'name': 'habilidades_disciplina',
                'id': 'habilidades_disciplina',
                'size': 15,
                'placeholder': 'Habilidades'
            }
        )
    )
        conteudo_disciplina = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'title': 'Conteudo',
                'type': 'text',
                'name': 'conteudo_disciplina',
                'id': 'conteudo_disciplina',
                'size': 15,
                'placeholder': 'Conteudo'
            }
        )
    )
        bibliografia_disciplina = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'title': 'Bibliografia',
                'type': 'text',
                'name': 'bibliografia_disciplina',
                'id': 'bibliografia_disciplina',
                'size': 20,
                'placeholder': 'Bibliografia'
            }
        )
    )
        bibliografia_complementar_disciplina = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'title': 'Bibliografia complementar',
                'type': 'text',
                'name': 'bibliografia_complementar_disciplina',
                'id': 'bibliografia_complementar_disciplina',
                'size': 20,
                'placeholder': 'Bibliografia complementar'
            }
        )
    )
        class Meta:
            model = Disciplina
            fields =    ['nome_disciplina',
                        'carga_horaria_disciplina',
                        'teoria_disciplina',
                        'pratica_disciplina',
                        'ementa_disciplina',
                        'competencias_disciplina',
                        'habilidades_disciplina',
                        'conteudo_disciplina',
                        'bibliografia_disciplina',
                        'bibliografia_complementar_disciplina']


class DisciplinofertadaForm(forms.ModelForm):
        ano_disciplina = forms.CharField(
        max_length=4,
        widget=forms.TextInput(
            attrs={
                'title': 'Ano',
                'type': 'number',
                'name': 'ano_disciplina',
                'id': 'ano_disciplina',
                'size': 5,
                'placeholder': 'Ano'
            }
        )
    )

            semestre_disciplina = forms.CharField(
            max_length=1,
            widget=forms.TextInput(
                attrs={
                    'title': 'Semestre',
                    'type': 'number',
                    'name': 'semestre_disciplina',
                    'id': 'semestre_disciplina',
                    'size': 5,
                    'placeholder': 'Semestre'
                }
            )
        )
        class Meta:
            model = Disciplina
            fields =    ['nome_disciplina',
                        'ano_disciplina',
                        'semestre_disciplina']



class GradeForm(forms.ModelForm):
        ano_grade = forms.CharField(
        max_length=4,
        widget=forms.TextInput(
            attrs={
                'title': 'Ano',
                'type': 'number',
                'name': 'ano_grade',
                'id': 'ano_grade',
                'size': 5,
                'placeholder': 'Ano'
            }
        )
    )

        semestre_grade = forms.CharField(
        max_length=1,
        widget=forms.TextInput(
            attrs={
                'title': 'Semestre',
                'type': 'number',
                'name': 'semestre_grade',
                'id': 'semestre_grade',
                'size': 5,
                'placeholder': 'Semestre'
            }
        )
    )
        class Meta:
            model = Grade
            fields =    ['sigla_curso',
                        'ano_grade',
                        'semestre_grade']


class PeriodoForm(forms.ModelForm):
        numero_periodo = forms.CharField(
        max_length=4,
        widget=forms.TextInput(
            attrs={
                'title': 'Numero',
                'type': 'number',
                'name': 'numero_periodo',
                'id': 'numero_periodo',
                'size': 5,
                'placeholder': 'Numero'
            }
        )
    )

        class Meta:
            model = Periodo
            fields =    ['sigla_curso',
                        'ano_grade',
                        'semestre_grade',
                        'numero_periodo']


class PeriododisciplinaForm(forms.ModelForm):
        class Meta:
            model = Periododisciplina
            fields =    ['sigla_curso',
                        'ano_grade',
                        'semestre_grade',
                        'numero_periodo',
                        'numero_periodo',
                        'nome_disciplina']

class ProfessorForm(forms.ModelForm):
        ra_professor = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'title': 'Ra',
                'type': 'text',
                'name': 'ra_professor',
                'id': 'ra_professor',
                'size': 5,
                'placeholder': 'Ra'
            }
        )
    )

        apelido_professor = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'title': 'Apelido',
                'type': 'text',
                'name': 'apelido_professor',
                'id': 'apelido_professor',
                'size': 10,
                'placeholder': 'Apelido'
            }
        )
    )

        nome_professor = forms.CharField(
        max_length=120,
        widget=forms.TextInput(
            attrs={
                'title': 'Nome',
                'type': 'text',
                'name': 'nome_professor',
                'id': 'nome_professor',
                'size': 15,
                'placeholder': 'Nome'
            }
        )
    )

        email_professor = forms.CharField(
        max_length=120,
        widget=forms.TextInput(
            attrs={
                'title': 'Email',
                'type': 'text',
                'name': 'email_professor',
                'id': 'email_professor',
                'size': 10,
                'placeholder': 'Email'
            }
        )
    )

        celular_professor = forms.CharField(
        max_length=120,
        widget=forms.TextInput(
            attrs={
                'title': 'Celular',
                'type': 'text',
                'name': 'celular_professor',
                'id': 'celular_professor',
                'size': 10,
                'placeholder': 'Celular'
            }
        )
    )
        class Meta:
            model = Professor
            fields =    ['ra_professor',
                        'apelido_professor',
                        'nome_professor',
                        'email_professor',
                        'celular_professor']
