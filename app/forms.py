from django import forms
from django.forms import ModelForm
from models import *
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class AlunoForm(forms.ModelForm):
    ra_aluno = forms.CharField(
    max_length=10,
    widget=forms.TextInput(
        attrs={
            'title': 'Ra',
            'type': 'number',
            'name': 'ra_aluno',
            'id': 'ra_aluno',
            'size': 10,
            'placeholder': 'Ra',
            'onkeypress' : 'validar(this); return numerico(event);'
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
            'placeholder': 'Nome',
            'onkeypress': 'return somenteletraacento(event)'
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
            'placeholder': 'Email',
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
            'placeholder': 'Celular',
            'onkeypress' : 'validar(this); return numerico(event);'
        }
    )
)
    class Meta:
        model = Aluno
        fields = ['ra_aluno', 'nome_aluno', 'email_aluno', 'celular_aluno', 'sigla_curso']

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
            'placeholder': 'Nome',
            'onkeypress': 'return somenteletraacento(event)'

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
            'placeholder': 'Sigla',
            'style': 'text-transform:uppercase',
            'onkeypress': 'return somenteletra(event)'
        }
    )
)
    class Meta:
        model = Curso
        fields =    ['nome_curso', 'sigla_curso']

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
            'placeholder': 'Nome da disciplina',
            'onkeypress': 'return somenteletraacento(event)'
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
            'placeholder': 'Carga horaria',
            'onkeypress' : 'validar(this); return numerico(event);'
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
            'placeholder': 'Teoria',
            'onkeypress' : 'validar(this); return numerico(event);'
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
            'placeholder': 'Pratica',
            'onkeypress' : 'validar(this); return numerico(event);'
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
            'placeholder': 'Ementa',
            'onkeypress': 'return somenteletraacento(event)'
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
            'placeholder': 'Competencias',
            'onkeypress': 'return somenteletraacento(event)'
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
            'placeholder': 'Habilidades',
            'onkeypress': 'return somenteletraacento(event)'
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
            'placeholder': 'Conteudo',
            'onkeypress': 'return somenteletraacento(event)'
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
            'placeholder': 'Bibliografia',
            'onkeypress': 'return somenteletraacento(event)'
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
            'placeholder': 'Bibliografia complementar',
            'onkeypress': 'return somenteletraacento(event)'
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
            'placeholder': 'Ano',
            'onkeypress' : 'validarano(this); return numerico(event);'
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
            'placeholder': 'Semestre',
            'onkeypress' : 'validarsemestre(this); return numerico(event);'
        }
    )
)
    class Meta:
        model = Disciplinofertada
        fields = [  'nome_disciplina',
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
            'placeholder': 'Ano',
            'onkeypress' : 'validarano(this); return numerico(event);'
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
            'placeholder': 'Semestre',
            'onkeypress' : 'validarsemestre(this); return numerico(event);'
        }
    )
)
    class Meta:
        model = Grade
        fields = [  'sigla_curso',
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
        fields = [  'sigla_curso',
                    'ano_grade',
                    'semestre_grade',
                    'numero_periodo']

class PerioddisciplinaForm(forms.ModelForm):
    class Meta:
        model = Perioddisciplina
        fields = [  'sigla_curso',
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
            'placeholder': 'Ra',
            'onkeypress' : 'validar(this); return numerico(event);'
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
            'placeholder': 'Apelido',
            'onkeypress': 'return somenteletraacento(event)'
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
            'placeholder': 'Nome',
            'onkeypress': 'return somenteletraacento(event)'
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
            'placeholder': 'Celular',
            'onkeypress' : 'validar(this); return numerico(event);'
        }
    )
)
    class Meta:
        model = Professor
        fields =[   'ra_professor',
                    'apelido_professor',
                    'nome_professor',
                    'email_professor',
                    'celular_professor']

class TurmaForm(forms.ModelForm):
    turno_turma = forms.CharField(
    max_length=15,
    widget=forms.TextInput(
        attrs={
            'title': 'Turma',
            'type': 'text',
            'name': 'turno_turma',
            'id': 'turno_turma',
            'size': 5,
            'placeholder': 'Turma'
        }
    )
)
    class Meta:
        model = Turma
        fields = [  'nome_disciplina',
                    'ano_disciplina',
                    'semestre_disciplina',
                    'turno_turma',
                    'ra_professor']


class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = [  'ra_aluno',
                    'nome_disciplina',
                    'ano_disciplina',
                    'semestre_disciplina',
                    'id_turma']

class CursturmaForm(forms.ModelForm):
    class Meta:
        model = Cursturma
        fields = [  'sigla_curso',
                    'nome_disciplina',
                    'ano_disciplina',
                    'semestre_disciplina',
                    'id_turma']

class QuestaoForm(forms.ModelForm):
    numero_questao = forms.CharField(
    max_length=5,
    widget=forms.TextInput(
        attrs={
            'title': 'Numero questao',
            'type': 'number',
            'name': 'numero_questao',
            'id': 'numero_questao',
            'size': 5,
            'placeholder': 'Numero questao'
        }
    )
)
    datalimiteentrega_questao = forms.CharField(
    max_length=5,
    widget=forms.TextInput(
        attrs={
            'title': 'Data limite entrega',
            'type': 'number',
            'name': 'datalimiteentrega_questao',
            'id': 'datalimiteentrega_questao',
            'size': 5,
            'placeholder': 'Data limite entrega'
        }
    )
)
    descricao_questao = forms.CharField(
    max_length=15,
    widget=forms.TextInput(
        attrs={
            'title': 'Descricao da questao',
            'type': 'text',
            'name': 'descricao_questao',
            'id': 'descricao_questao',
            'size': 15,
            'placeholder': 'Descricao da questao'
        }
    )
)
    data_questao = forms.CharField(
    max_length=15,
    widget=forms.TextInput(
        attrs={
            'title': 'Data',
            'type': 'text',
            'name': 'data_questao',
            'id': 'data_questao',
            'size': 5,
            'placeholder': 'Data'
        }
    )
)
    class Meta:
        model = Questao
        fields = [  'nome_disciplina',
                    'ano_disciplina',
                    'semestre_disciplina',
                    'id_turma',
                    'numero_questao',
                    'datalimiteentrega_questao',
                    'descricao_questao',
                    'data_questao']

class RespostaForm(forms.ModelForm):
    dataavaliacao_resposta = forms.CharField(
    max_length=15,
    widget=forms.TextInput(
        attrs={
            'title': 'Data da avaliacao',
            'type': 'text',
            'name': 'dataavaliacao_resposta',
            'id': 'dataavaliacao_resposta',
            'size': 10,
            'placeholder': 'Data da avaliacao'
        }
    )
)
    nota_resposta = forms.CharField(
    max_length=5,
    widget=forms.TextInput(
        attrs={
            'title': 'Nota',
            'type': 'text',
            'name': 'nota_resposta',
            'id': 'nota_resposta',
            'size': 5,
            'placeholder': 'Nota'
        }
    )
)
    avaliacao_resposta = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'title': 'Avaliacao',
            'type': 'text',
            'name': 'avaliacao_resposta',
            'id': 'avaliacao_resposta',
            'size': 15,
            'placeholder': 'Avaliacao'
        }
    )
)
    descricao_resposta = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
        attrs={
            'title': 'Descricao',
            'type': 'text',
            'name': 'descricao_resposta',
            'id': 'descricao_resposta',
            'size': 15,
            'placeholder': 'Descricao'
        }
    )
)
    datadeenvio_resposta = forms.CharField(
    max_length=15,
    widget=forms.TextInput(
        attrs={
            'title': 'Data de envio',
            'type': 'text',
            'name': 'datadeenvio_resposta',
            'id': 'datadeenvio_resposta',
            'size': 10,
            'placeholder': 'Data de envio'
        }
    )
)

    class Meta:
        model = Resposta
        fields = [  'nome_disciplina',
                    'ano_disciplina',
                    'semestre_disciplina',
                    'id_turma',
                    'numero_questao',
                    'ra_aluno',
                    'dataavaliacao_resposta',
                    'nota_resposta',
                    'avaliacao_resposta',
                    'descricao_resposta',
                    'datadeenvio_resposta']


class ArquivrespostaForm(forms.ModelForm):
    arquivo_resposta = forms.CharField(
    max_length=500,
    widget=forms.TextInput(
        attrs={
            'title': 'Arquivo resposta',
            'type': 'text',
            'name': 'arquivo_resposta',
            'id': 'arquivo_resposta',
            'size': 10,
            'placeholder': 'Arquivo resposta'
        }
    )
)

    class Meta:
        model = Arquivresposta
        fields = [  'nome_disciplina',
                    'ano_disciplina',
                    'semestre_disciplina',
                    'id_turma',
                    'numero_questao',
                    'ra_aluno',
                    'arquivo_resposta']

class ArquivquestaoForm(forms.ModelForm):
    arquivo_questao = forms.CharField(
    max_length=500,
    widget=forms.TextInput(
        attrs={
            'title': 'Arquivo questao',
            'type': 'text',
            'name': 'arquivo_questao',
            'id': 'arquivo_questao',
            'size': 10,
            'placeholder': 'Arquivo questao'
        }
    )
)

    class Meta:
        model = Arquivquestao
        fields = [  'nome_disciplina',
                    'ano_disciplina',
                    'semestre_disciplina',
                    'id_turma',
                    'numero_questao',
                    'arquivo_questao']
