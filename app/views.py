from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from models import *
from forms import *
from datetime import datetime
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

def listar_aluno(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/aluno/listar_aluno.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de aluno',
            'alunos': Aluno.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_aluno(request, template_name='app/aluno/novo_aluno.html'):
    curso = Curso.objects.all()
    sigla_curso = request.POST.get('sigla_curso')
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.sigla_curso = Curso.objects.get(sigla_curso = sigla_curso)
        form.save()
        return redirect('listar_aluno')
    return render(request, template_name, {'form':form, 'curso': curso})

def apagar_aluno(request, pk, template_name='app/aluno/confirmacao_apagar_aluno.html'):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method=='POST':
        aluno.delete()
        return redirect('listar_aluno')
    return render(request, template_name, {'object':aluno.nome_aluno})

def editar_aluno(request, pk, template_name='app/aluno/novo_aluno.html'):
    aluno= get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance = aluno)
    if form.is_valid():
        form.save()
        return redirect('listar_aluno')
    return render(request, template_name, {'form':form})

def apagar_aluno(request, pk, template_name='app/aluno/confirmacao_apagar_aluno.html'):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method=='POST':
        aluno.delete()
        return redirect('listar_aluno')
    return render(request, template_name, {'object':aluno.nome_aluno})

def listar_curso(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/curso/listar_curso.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de curso',
            'cursos': Curso.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_curso(request, template_name='app/curso/novo_curso.html'):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_curso')
    return render(request, template_name, {'form':form})

def apagar_curso(request, pk, template_name='app/curso/confirmacao_apagar_curso.html'):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method=='POST':
        curso.delete()
        return redirect('listar_curso')
    return render(request, template_name, {'object':curso.nome_curso})

def editar_curso(request, pk, template_name='app/curso/novo_curso.html'):
    if request.user.is_superuser:
        curso = get_object_or_404(Curso, pk=pk)
    else:
        curso = get_object_or_404(Curso, pk=pk)
    form = CursoForm(request.POST or None, instance = curso)
    if form.is_valid():
        form.save()
        return redirect('listar_curso')
    return render(request, template_name, {'form':form})

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
    return render(request, template_name, {'object':disciplina.nome_disciplina})

def editar_disciplina(request, pk, template_name='app/disciplina/novo_disciplina.html'):
    if request.user.is_superuser:
        disciplina = get_object_or_404(Disciplina, pk=pk)
    else:
        disciplina = get_object_or_404(Disciplina, pk=pk)
    form = DisciplinaForm(request.POST or None, instance = disciplina)
    if form.is_valid():
        form.save()
        return redirect('listar_disciplina')
    return render(request, template_name, {'form':form})


def listar_professor(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/professor/listar_professor.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de professor',
            'professors': Professor.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_professor(request, template_name='app/professor/novo_professor.html'):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_professor')
    return render(request, template_name, {'form':form})

def apagar_professor(request, pk, template_name='app/professor/confirmacao_apagar_professor.html'):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method=='POST':
        professor.delete()
        return redirect('listar_professor')
    return render(request, template_name, {'object':professor.nome_professor})

def editar_professor(request, pk, template_name='app/professor/novo_professor.html'):
    if request.user.is_superuser:
        professor = get_object_or_404(Professor, pk=pk)
    else:
        professor = get_object_or_404(Professor, pk=pk)
    form = ProfessorForm(request.POST or None, instance = professor)
    if form.is_valid():
        form.save()
        return redirect('listar_professor')
    return render(request, template_name, {'form':form})

def listar_grade(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/grade/listar_grade.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de grade',
            'grades': Grade.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_grade(request, template_name='app/grade/novo_grade.html'):
    curso = Curso.objects.all()
    sigla_curso = request.POST.get('sigla_curso')
    form = GradeForm(request.POST or None)
    if form.is_valid():
        form.sigla_curso = Curso.objects.get(sigla_curso = sigla_curso)
        form.save()
        return redirect('listar_grade')
    return render(request, template_name, {'form':form, 'curso': curso})

def apagar_grade(request, pk, template_name='app/grade/confirmacao_apagar_grade.html'):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method=='POST':
        grade.delete()
        return redirect('listar_grade')
    return render(request, template_name, {'object':grade.sigla_curso})

def editar_grade(request, pk, template_name='app/grade/novo_grade.html'):
    if request.user.is_superuser:
        grade = get_object_or_404(Grade, pk=pk)
    else:
        grade = get_object_or_404(Grade, pk=pk)
    form = GradeForm(request.POST or None, instance = grade)
    if form.is_valid():
        form.save()
        return redirect('listar_grade')
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

def novo_grade(request, template_name='app/periodo/novo_periodo.html'):
    curso = Curso.objects.all()
    sigla_curso = request.POST.get('sigla_curso')
    grade = Grade.objects.all()
    ano_grade = request.POST.get('ano_grade')
    semestre_grade = request.POST.get('semestre_grade')
    form = PeriodoForm(request.POST or None)
    if form.is_valid():
        form.sigla_curso = Curso.objects.get(sigla_curso = sigla_curso)
        form.ano_grade = Grade.objects.get(ano_grade = ano_grade)
        form.semestre_grade = Grade.objects.get(semestre_grade = semestre_grade)
        form.save()
        return redirect('listar_periodo')
    return render(request, template_name, {'form':form, 'curso': curso, 'grade': grade})

def apagar_periodo(request, pk, template_name='app/periodo/confirmacao_apagar_periodo.html'):
    periodo = get_object_or_404(Periodo, pk=pk)
    if request.method=='POST':
        periodo.delete()
        return redirect('listar_periodo')
    return render(request, template_name, {'object':periodo.numero_periodo})

def editar_periodo(request, pk, template_name='app/periodo/novo_periodo.html'):
    if request.user.is_superuser:
        periodo = get_object_or_404(Periodo, pk=pk)
    else:
        periodo = get_object_or_404(Periodo, pk=pk)
    form = PeriodoForm(request.POST or None, instance = periodo)
    if form.is_valid():
        form.save()
        return redirect('listar_periodo')
    return render(request, template_name, {'form':form})
