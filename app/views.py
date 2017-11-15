from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext

from app.models import *
from app.forms import *

from datetime import datetime
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def pagina_inicial(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Pagina inicial',
            'year':datetime.now().year,
        })
    )

def listar_alunos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/aluno/listar_alunos.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de alunos',
            'alunos': Aluno.objects.all(),
            'year':datetime.now().year,
        })
    )


def listar_professor(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/professor/listar_professor.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de professores',
            'professores': Professor.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_professor(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/professor/novo_candidato.html',
        context_instance = RequestContext(request,
        {
            'title':'Novo professor',
            'message':'Novo professor',
            'year':datetime.now().year,
        })
    )


def listar_cursos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/curso/listar_cursos.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de cursos',
            'cursos': Curso.objects.all(),
            'year':datetime.now().year,
        })
    )


def listar_disciplina(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/disciplina/listar_disciplina.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de disciplina',
            'disciplinas': Disciplina.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_curso(request, template_name='app/curso/novo_curso.html'):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_cursos')
    return render(request, template_name, {'form':form})

def novo_aluno(request, template_name='app/aluno/novo_aluno.html'):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_alunos')
    return render(request, template_name, {'form':form})

def novo_professor(request, template_name='app/professor/novo_professor.html'):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_professor')
    return render(request, template_name, {'form':form})

def novo_colaborador(request, template_name='app/colaborador/novo_colaborador.html'):
    form = ColaboradorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_colaborador')
    return render(request, template_name, {'form':form})

def novo_disciplina(request, template_name='app/disciplina/novo_disciplina.html'):
    form = DisciplinaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_disciplina')
    return render(request, template_name, {'form':form})

def apagar_disciplina(request, pk, template_name='app/disciplina/confirmacao_apagar_disciplina.html'):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    if request.method=='POST':
        disciplina.delete()
        return redirect('listar_disciplina')
    return render(request, template_name, {'object':disciplina.nome})


def apagar_aluno(request, pk, template_name='app/aluno/confirmacao_apagar_aluno.html'):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method=='POST':
        aluno.delete()
        return redirect('listar_alunos')
    return render(request, template_name, {'object':aluno.nome_aluno})

def apagar_professor(request, pk, template_name='app/professor/confirmacao_apagar_candidato.html'):
    candidato = get_object_or_404(Candidato, pk=pk)
    if request.method=='POST':
        candidato.delete()
        return redirect('listar_professor')
    return render(request, template_name, {'object':candidato.nome})

def apagar_curso(request, pk, template_name='app/curso/confirmacao_apagar_curso.html'):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method=='POST':
        curso.delete()
        return redirect('listar_cursos')
    return render(request, template_name, {'object':curso.nome_curso})


def editar_aluno(request, pk, template_name='app/aluno/novo_aluno.html'):
    aluno= get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance = aluno)
    if form.is_valid():
        form.save()
        return redirect('listar_alunos')
    return render(request, template_name, {'form':form})

def editar_usuario(request, pk, template_name='app/disciplina/novo_disciplina.html'):
    disciplina= get_object_or_404(Disciplina, pk=pk)
    form = DisciplinaForm(request.POST or None, instance = disciplina)
    if form.is_valid():
        form.save()
        return redirect('lista_disciplina')
    return render(request, template_name, {'form':form})

def editar_professor(request, pk, template_name='app/professor/novo_candidato.html'):
    if request.user.is_superuser:
        candidato= get_object_or_404(Professor, pk=pk)
    else:
        candidato= get_object_or_404(Professor, pk=pk)
    form = ProfessorForm(request.POST or None, instance = professor)
    if form.is_valid():
        form.save()
        return redirect('listar_professor')
    return render(request, template_name, {'form':form})

def editar_curso(request, pk, template_name='app/curso/novo_curso.html'):
    if request.user.is_superuser:
        curso = get_object_or_404(Curso, pk=pk)
    else:
        curso = get_object_or_404(Curso, pk=pk)
    form = CursoForm(request.POST or None, instance = curso)
    if form.is_valid():
        form.save()
        return redirect('listar_cursos')
    return render(request, template_name, {'form':form})


def listar_matricula(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/matricula/listar_matricula.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de matricula',
            'matriculas': Matricula.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_matricula(request, template_name='app/matricula/novo_matricula.html'):
    form = MatriculaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_matricula')
    return render(request, template_name, {'form':form})

def apagar_matricula(request, pk, template_name='app/matricula/confirmacao_apagar_matricula.html'):
    matricula = get_object_or_404(Matricula, pk=pk)
    if request.method=='POST':
        matricula.delete()
        return redirect('listar_matricula')
    return render(request, template_name, {'object':matricula.ra_aluno_matricula})


def editar_matricula(request, pk, template_name='app/matricula/novo_matricula.html'):
    if request.user.is_superuser:
        matricula = get_object_or_404(Matricula, pk=pk)
    else:
        matricula = get_object_or_404(Matricula, pk=pk)
    form = MatriculaForm(request.POST or None, instance = matricula)
    if form.is_valid():
        form.save()
        return redirect('listar_matricula')
    return render(request, template_name, {'form':form})


def listar_grade_curricular(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/grade_curricular/listar_grade_curricular.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de grade curricular',
            'gradecurriculars': GradeCurricular.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_grade_curricular(request, template_name='app/grade_curricular/novo_grade_curricular.html'):
    form = GradeCurricularForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_gradecurricular')
    return render(request, template_name, {'form':form})

def apagar_grade_curricular(request, pk, template_name='app/grade_curricular/confirmacao_apagar_grade_curricular.html'):
    gradecurricular = get_object_or_404(GradeCurricular, pk=pk)
    if request.method=='POST':
        gradecurricular.delete()
        return redirect('listar_grade_curricular')
    return render(request, template_name, {'object':gradecurricular.sigla_curso_grade_curricular})

def editar_grade_curricular(request, pk, template_name='app/grade_curricular/novo_grade_curricular.html'):
    if request.user.is_superuser:
        gradecurricular = get_object_or_404(GradeCurricular, pk=pk)
    else:
        gradecurricular = get_object_or_404(GradeCurricular, pk=pk)
    form = GradeCurricularForm(request.POST or None, instance = gradecurricular)
    if form.is_valid():
        form.save()
        return redirect('listar_grade_curricular')
    return render(request, template_name, {'form':form})


def listar_periodo(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/periodo/listar_periodo.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de periodo',
            'periodos': Periodo.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_periodo(request, template_name='app/periodo/novo_periodo.html'):
    form = PeriodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_periodo')
    return render(request, template_name, {'form':form})

def apagar_periodo(request, pk, template_name='app/periodo/confirmacao_apagar_periodo.html'):
    periodo = get_object_or_404(Periodo, pk=pk)
    if request.method=='POST':
        periodo.delete()
        return redirect('listar_periodo')
    return render(request, template_name, {'object':periodo.sigla_curso_periodo})

def editar__periodo(request, pk, template_name='app/periodo/novo_periodo.html'):
    if request.user.is_superuser:
        periodo = get_object_or_404(Periodo, pk=pk)
    else:
        periodo = get_object_or_404(Periodo, pk=pk)
    form = PeriodoForm(request.POST or None, instance = periodo)
    if form.is_valid():
        form.save()
        return redirect('listar_periodo')
    return render(request, template_name, {'form':form})
