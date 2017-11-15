from django import forms
from django.forms import ModelForm
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
            fields =    ['ra_aluno',
                        'nome_aluno',
                        'email_aluno',
                        'celular_aluno',
                        'curso_aluno']


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
