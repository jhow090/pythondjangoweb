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

def novo_aluno(request):
    aluno = Aluno.object.all()
    cname = request.POST.get('curso_aluno')
    if request.method == 'GET':
        form = AlunoForm()
    else:
        aluno = Aluno.objects.get(cname = cname)
        aluno.delete()
        return redirect('lista_aluno')
    return render(request, 'app/novo_aluno.html', {'form': form, 'aluno': aluno})

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
