from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from models import *

from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

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
    max_length=15,
    widget=forms.TextInput(
        attrs={
            'title': 'Email',
            'type': 'text',
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
            'type': 'text',
            'name': 'celular_aluno',
            'id': 'celular_aluno',
            'size': 10,
            'placeholder': 'Celular'
        }
    )
)


    class Meta:
        model = Aluno
        fields = ['ra_aluno', 'nome_aluno', 'email_aluno', 'celular_aluno', 'curso_aluno']


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        error_messages = {
            'first_name': {
                'required': 'first_name'
            }
        }

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
        fields = ['nome_curso', 'sigla_curso']


class ProfessorForm(forms.ModelForm):
    ra_professor = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'title': 'Ra',
            'type': 'number',
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
    max_length=100,
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
    max_length=15,
    widget=forms.TextInput(
        attrs={
            'title': 'Email',
            'type': 'text',
            'name': 'email_professor',
            'id': 'email_professor',
            'size': 15,
            'placeholder': 'Email'
        }
    )
)
    celular_professor = forms.CharField(
    max_length=15,
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
        fields = ['ra_professor', 'apelido_professor', 'nome_professor', 'email_professor', 'celular_professor']

class MatriculaForm(forms.ModelForm):
    ra_aluno_matricula = forms.CharField(
    max_length=10,
    widget=forms.TextInput(
        attrs={
            'title': 'Ra',
            'type': 'number',
            'name': 'ra_aluno_matricula',
            'id': 'ra_aluno_matricula',
            'size': 10,
            'placeholder': 'Ra'
        }
    )
)
    nome_disciplina_matricula = forms.CharField(
    max_length=200,
    widget=forms.TextInput(
        attrs={
            'title': 'Nome da disciplina',
            'type': 'text',
            'name': 'nome_disciplina_matricula',
            'id': 'nome_disciplina_matricula',
            'size': 35,
            'placeholder': 'Nome da disciplina'
        }
    )
)
    ano_ofertado_matricula = forms.CharField(
    max_length=10,
    widget=forms.TextInput(
        attrs={
            'title': 'Ano',
            'type': 'text',
            'name': 'ano_ofertado_matricula',
            'id': 'ano_ofertado_matricula',
            'size': 5,
            'placeholder': 'Ano'
        }
    )
)

    semestre_ofertado_matricula = forms.CharField(
    max_length=10,
    widget=forms.TextInput(
        attrs={
            'title': 'Semestre',
            'type': 'text',
            'name': 'semestre_ofertado_matricula',
            'id': 'semestre_ofertado_matricula',
            'size': 5,
            'placeholder': 'Semestre'
        }
    )
)

    id_turma_matricula = forms.CharField(
    max_length=10,
    widget=forms.TextInput(
        attrs={
            'title': 'Turma',
            'type': 'text',
            'name': 'id_turma_matricula',
            'id': 'id_turma_matricula',
            'size': 10,
            'placeholder': 'Turma'
        }
    )
)
    class Meta:
        model = Matricula
        fields = ['ra_aluno_matricula', 'nome_disciplina_matricula', 'ano_ofertado_matricula', 'semestre_ofertado_matricula', 'id_turma_matricula']

class DisciplinaForm(forms.ModelForm):
    nome_disciplina = forms.CharField(
    max_length=200,
    widget=forms.TextInput(
        attrs={
            'title': 'Nome da disciplina',
            'type': 'text',
            'name': 'nome_disciplina',
            'id': 'nome_disciplina',
            'size': 25,
            'placeholder': 'Nome da disciplina'
        }
    )
)

    carga_horaria_disciplina = forms.CharField(
    max_length=100,
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
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'title': 'Teoria',
            'type': 'text',
            'name': 'teoria_disciplina',
            'id': 'teoria_disciplina',
            'size': 10,
            'placeholder': 'Teoria'
        }
    )
)

    pratica_disciplina = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'title': 'Pratica',
            'type': 'text',
            'name': 'pratica_disciplina',
            'id': 'pratica_disciplina',
            'size': 10,
            'placeholder': 'Pratica'
        }
    )
)

    ementa_disciplina = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'title': 'Ementa',
            'type': 'text',
            'name': 'ementa_disciplina',
            'id': 'ementa_disciplina',
            'size': 35,
            'placeholder': 'Ementa'
        }
    )
)

    competencias_disciplina = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'title': 'Competencias',
            'type': 'text',
            'name': 'competencias_disciplina',
            'id': 'competencias_disciplina',
            'size': 35,
            'placeholder': 'Competencias'
        }
    )
)

    habilidades_disciplina = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'title': 'Habilidades',
            'type': 'text',
            'name': 'habilidades_disciplina',
            'id': 'habilidades_disciplina',
            'size': 35,
            'placeholder': 'Habilidades'
        }
    )
)

    conteudo_disciplina = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'title': 'Conteudo',
            'type': 'text',
            'name': 'conteudo_disciplina',
            'id': 'conteudo_disciplina',
            'size': 35,
            'placeholder': 'Conteudo'
        }
    )
)

    bibliografia_disciplina = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'title': 'Bibliografia',
            'type': 'text',
            'name': 'bibliografia_disciplina',
            'id':  'bibliografia_disciplina',
            'size': 35,
            'placeholder': 'Bibliografia'
        }
    )
)

    bibliografia_complementar_disciplina = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'title': 'Bibliografia complementar',
            'type': 'text',
            'name': 'bibliografia_complementar',
            'id':  'bibliografia_complementar',
            'size': 35,
            'placeholder': 'Bibliografia complementar'
        }
    )
)
    class Meta:
        model = Disciplina
        fields = [  'nome_disciplina',
                    'carga_horaria_disciplina',
                    'teoria_disciplina',
                    'pratica_disciplina',
                    'ementa_disciplina',
                    'competencias_disciplina',
                    'habilidades_disciplina',
                    'conteudo_disciplina',
                    'bibliografia_disciplina',
                    'bibliografia_complementar_disciplina']

class GradeCurricularForm(forms.ModelForm):
    sigla_curso_grade_curricular = forms.CharField(
    max_length=5,
    widget=forms.TextInput(
        attrs={
            'title': 'Sigla do curso',
            'type': 'text',
            'name': 'sigla_curso_grade_curricular',
            'id': 'sigla_curso_grade_curricular',
            'size': 25,
            'placeholder': 'Sigla do curso'
        }
    )
)

    ano_grade_curricular = forms.CharField(
    max_length=5,
    widget=forms.TextInput(
        attrs={
            'title': 'Ano',
            'type': 'text',
            'name': 'ano_grade_curricular',
            'id': 'ano_grade_curricular',
            'size': 10,
            'placeholder': 'Ano'
        }
    )
)

    semeste_grade_curricular = forms.CharField(
    max_length=5,
    widget=forms.TextInput(
        attrs={
            'title': 'Semestre',
            'type': 'text',
            'name': 'semeste_grade_curricular',
            'id': 'semeste_grade_curricular',
            'size': 10,
            'placeholder': 'Semestre'
        }
    )
)

    class Meta:
        model = GradeCurricular
        fields = [  'sigla_curso_grade_curricular',
                    'ano_grade_curricular',
                    'semeste_grade_curricular']

class PeriodoForm(forms.ModelForm):
    sigla_curso_periodo = forms.CharField(
    max_length=5,
    widget=forms.TextInput(
        attrs={
            'title': 'Sigla do curso',
            'type': 'text',
            'name': 'sigla_curso_periodo',
            'id': 'sigla_curso_periodo',
            'size': 25,
            'placeholder': 'Sigla do curso'
        }
    )
)

    ano_grade_curricular_periodo = forms.CharField(
    max_length=5,
    widget=forms.TextInput(
        attrs={
            'title': 'Ano',
            'type': 'text',
            'name': 'ano_grade_curricular_periodo',
            'id': 'ano_grade_curricular_periodo',
            'size': 10,
            'placeholder': 'Ano'
        }
    )
)

    semestre_grade_curricular_periodo = forms.CharField(
    max_length=5,
    widget=forms.TextInput(
        attrs={
            'title': 'Semestre',
            'type': 'text',
            'name': 'semestre_grade_curricular_periodo',
            'id': 'semestre_grade_curricular_periodo',
            'size': 10,
            'placeholder': 'Semestre'
        }
    )
)

    class Meta:
        model = Periodo
        fields = [  'sigla_curso_periodo',
                    'ano_grade_curricular_periodo',
                    'semestre_grade_curricular_periodo']
