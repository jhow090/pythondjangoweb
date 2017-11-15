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
            'size': 35,
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
            'size': 35,
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
            'size': 25,
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
            'size': 10,
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
            'size': 35,
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
            'size': 35,
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
            'size': 35,
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
        model = Professor
        fields = ['ra_aluno_matricula', 'nome_disciplina_matricula', 'ano_ofertado_matricula', 'semestre_ofertado_matricula', 'id_turma_matricula']



class ColaboradorForm(forms.ModelForm):

    nome = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'size': 35,
            'placeholder': 'Nome'
        }
    )
)

    data_nascimento = forms.CharField(
    max_length=15,
    widget=forms.TextInput(
        attrs={
            'size': 15,
            'placeholder': 'Data de nascimento'
        }
    )
)

    email = forms.CharField(
    max_length=15,
    widget=forms.TextInput(
        attrs={
            'size': 35,
            'placeholder': 'Email'
        }
    )
)

    endereco = forms.CharField(
    max_length=200,
    widget=forms.TextInput(
        attrs={
            'size': 35,
            'placeholder': 'Endereco'
        }
    )
)

    cidade = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'size': 10,
            'placeholder': 'Cidade'
        }
    )
)

    estado = forms.CharField(
    max_length=10,
    widget=forms.TextInput(
        attrs={
            'size': 5,
            'placeholder': 'Estado'
        }
    )
)

    telefone = forms.CharField(
    max_length=15,
    widget=forms.TextInput(
        attrs={
            'size': 10,
            'placeholder': 'Telefone'
        }
    )
)

    celular = forms.CharField(
    max_length=15,
    widget=forms.TextInput(
        attrs={
            'size': 10,
            'placeholder': 'Celular'
        }
    )
)

    class Meta:
        model = Colaborador
        fields = ['nome', 'cargo', 'data_nascimento', 'email', 'endereco', 'cidade', 'estado', 'telefone', 'celular']

class UsuarioForm(forms.ModelForm):

    nome = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'size': 25,
            'placeholder': 'Nome'
        }
    )
)

    email = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'size': 25,
            'placeholder': 'Email'
        }
    )
)

    senha = forms.CharField(
    max_length=15,
    widget=forms.TextInput(
        attrs={
            'size': 25,
            'placeholder': 'Senha'
        }
    )
)

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']
