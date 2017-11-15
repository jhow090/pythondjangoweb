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
            'title':'Cadastro de alunos',
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
            'title':'Cadastro de professores',
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


def listar_colaborador(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/colaborador/listar_colaborador.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de colaborador',
            'colaboradores': Colaborador.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_colaborador(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/colaborador/novo_colaborador.html',
        context_instance = RequestContext(request,
        {
            'title':'Novo colaborador',
            'message':'Novo colaborador',
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
            'title':'Cadastro de cursos',
            'cursos': Curso.objects.all(),
            'year':datetime.now().year,
        })
    )


def listar_usuarios(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/usuario/listar_usuarios.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de usuarios',
            'usuarios': Usuario.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_usuario(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/usuario/novo_usuario.html',
        context_instance = RequestContext(request,
        {
            'title':'Novo usuario',
            'message':'Novo usuario',
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

def novo_usuario(request, template_name='app/usuario/novo_usuario.html'):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_usuarios')
    return render(request, template_name, {'form':form})

def apagar_usuario(request, pk, template_name='app/usuario/confirmacao_apagar_usuario.html'):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method=='POST':
        usuario.delete()
        return redirect('listar_usuario')
    return render(request, template_name, {'object':usuario.nome})


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

def apagar_colaborador(request, pk, template_name='app/colaborador/confirmacao_apagar_colaborador.html'):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method=='POST':
        colaborador.delete()
        return redirect('listar_colaborador')
    return render(request, template_name, {'object':colaborador.nome})

def apagar_curso(request, pk, template_name='app/curso/confirmacao_apagar_curso.html'):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method=='POST':
        curso.delete()
        return redirect('listar_cursos')
    return render(request, template_name, {'object':curso.nome_curso})


def editar_aluno(request, pk, template_name='app/aluno/editar_aluno.html'):
    form = AlunoForm(request.POST or None, instance = aluno)
    if form.is_valid():
        form.save()
        return redirect('listar_alunos')
    return render(request, template_name, {'form':form})

def editar_usuario(request, pk, template_name='app/usuario/novo_usuario.html'):
    usuario= get_object_or_404(Usuario, pk=pk)
    form = UsuarioForm(request.POST or None, instance = usuario)
    if form.is_valid():
        form.save()
        return redirect('lista_usuarios')
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

def editar_colaborador(request, pk, template_name='app/colaborador/novo_colaborador.html'):
    if request.user.is_superuser:
        colaborador= get_object_or_404(Colaborador, pk=pk)
    else:
        colaborador= get_object_or_404(Colaborador, pk=pk)
    form = ColaboradorForm(request.POST or None, instance = colaborador)
    if form.is_valid():
        form.save()
        return redirect('listar_colaborador')
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
            'title':'Cadastro de matricula',
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
