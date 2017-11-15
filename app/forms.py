from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from models import Curso
from models import Aluno
from models import Candidato
from models import Colaborador
from models import Usuario
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


class CandidatoForm(forms.ModelForm):
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
        model = Candidato
        fields = ['nome', 'curso', 'data_nascimento', 'email', 'endereco', 'cidade', 'estado', 'telefone', 'celular']

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
