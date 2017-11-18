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
    title = 'Aluno'
    curso = Curso.objects.all()
    sigla_curso = request.POST.get('sigla_curso')
    form = AlunoForm(request.POST or None)
    if form.is_valid():
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

def novo_periodo(request, template_name='app/periodo/novo_periodo.html'):
    curso = Curso.objects.all()
    sigla_curso = request.POST.get('sigla_curso')
    grade = Grade.objects.all()
    ano_grade = request.POST.get('ano_grade')
    semestre_grade = request.POST.get('semestre_grade')
    form = PeriodoForm(request.POST or None)
    if form.is_valid():
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

def listar_perioddisciplina(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/perioddisciplina/listar_perioddisciplina.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de periodo disciplina',
            'perioddisciplinas': Perioddisciplina.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_perioddisciplina(request, template_name='app/perioddisciplina/novo_perioddisciplina.html'):
    disciplina = Disciplina.objects.all()
    nome_disciplina = request.POST.get('nome_disciplina')
    periodo = Periodo.objects.all()
    sigla_curso = request.POST.get('sigla_curso')
    ano_grade = request.POST.get('ano_grade')
    semestre_grade = request.POST.get('semestre_grade')
    numero_periodo = request.POST.get('numero_periodo')
    form = PerioddisciplinaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_perioddisciplina')
    return render(request, template_name, {'form':form, 'disciplina': disciplina, 'periodo': periodo})

def apagar_perioddisciplina(request, pk, template_name='app/periododisciplina/confirmacao_apagar_periododisciplina.html'):
    perioddisciplina = get_object_or_404(Perioddisciplina, pk=pk)
    if request.method=='POST':
        perioddisciplina.delete()
        return redirect('listar_perioddisciplina')
    return render(request, template_name, {'object':perioddisciplina.nome_disciplina})

def editar_perioddisciplina(request, pk, template_name='app/perioddisciplina/novo_perioddisciplina.html'):
    if request.user.is_superuser:
        perioddisciplina = get_object_or_404(Perioddisciplina, pk=pk)
    else:
        perioddisciplina = get_object_or_404(Perioddisciplina, pk=pk)
    form = PerioddisciplinaForm(request.POST or None, instance = perioddisciplina)
    if form.is_valid():
        form.save()
        return redirect('listar_perioddisciplina')
    return render(request, template_name, {'form':form})


def listar_disciplinofertada(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/disciplinofertada/listar_disciplinofertada.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de disciplina ofertada',
            'disciplinofertadas': Disciplinofertada.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_disciplinofertada(request, template_name='app/disciplinofertada/novo_disciplinofertada.html'):
    disciplina = Disciplina.objects.all()
    nome_disciplina = request.POST.get('nome_disciplina')
    form = DisciplinofertadaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_disciplinofertada')
    return render(request, template_name, {'form':form, 'disciplina': disciplina})

def apagar_disciplinofertada(request, pk, template_name='app/disciplinofertada/confirmacao_apagar_disciplinofertada.html'):
    disciplinofertada = get_object_or_404(Disciplinofertada, pk=pk)
    if request.method=='POST':
        disciplinofertada.delete()
        return redirect('listar_disciplinofertada')
    return render(request, template_name, {'object':disciplinofertada.nome_disciplina})

def editar_disciplinofertada(request, pk, template_name='app/disciplinofertada/novo_disciplinofertada.html'):
    if request.user.is_superuser:
        disciplinofertada = get_object_or_404(Disciplinofertada, pk=pk)
    else:
        disciplinofertada = get_object_or_404(Disciplinofertada, pk=pk)
    form = DisciplinofertadaForm(request.POST or None, instance = Disciplinofertada)
    if form.is_valid():
        form.save()
        return redirect('listar_disciplinofertada')
    return render(request, template_name, {'form':form})

def listar_turma(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/turma/listar_turma.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de turma',
            'turmas': Turma.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_turma(request, template_name='app/turma/novo_turma.html'):
    disciplinofertada = Disciplinofertada.objects.all()
    nome_disciplina = request.POST.get('nome_disciplina')
    ano_disciplina = request.POST.get('ano_disciplina')
    semestre_disciplina = request.POST.get('semestre_disciplina')
    professor = Professor.objects.all()
    ra_professor = request.POST.get('ra_professor')
    form = TurmaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_turma')
    return render(request, template_name, { 'form':form, 'disciplinofertada': disciplinofertada, 'professor': professor})

def apagar_turma(request, pk, template_name='app/turma/confirmacao_apagar_turma.html'):
    turma = get_object_or_404(Turma, pk=pk)
    if request.method=='POST':
        turma.delete()
        return redirect('listar_turma')
    return render(request, template_name, {'object':turma.turno_turma})

def editar_turma(request, pk, template_name='app/turma/novo_turma.html'):
    if request.user.is_superuser:
        turma = get_object_or_404(Turma, pk=pk)
    else:
        turma = get_object_or_404(Turma, pk=pk)
    form = TurmaForm(request.POST or None, instance = Turma)
    if form.is_valid():
        form.save()
        return redirect('listar_turma')
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
    aluno = Aluno.objects.all()
    ra_aluno = request.POST.get('ra_aluno')
    disciplinofertada = Disciplinofertada.objects.all()
    nome_disciplina = request.POST.get('nome_disciplina')
    ano_disciplina = request.POST.get('ano_disciplina')
    semestre_disciplina = request.POST.get('semestre_disciplina')
    turma = Turma.objects.all()
    id_turma = request.POST.get('id_turma')
    form = MatriculaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_matricula')
    return render(request, template_name, { 'form':form, 'aluno': aluno, 'disciplinofertada': disciplinofertada, 'turma': turma})

def apagar_matricula(request, pk, template_name='app/matricula/confirmacao_apagar_matricula.html'):
    matricula = get_object_or_404(Matricula, pk=pk)
    if request.method=='POST':
        matricula.delete()
        return redirect('listar_matricula')
    return render(request, template_name, {'object':matricula.ra_aluno})

def editar_matricula(request, pk, template_name='app/matricula/novo_matricula.html'):
    if request.user.is_superuser:
        matricula = get_object_or_404(Matricula, pk=pk)
    else:
        matricula = get_object_or_404(Matricula, pk=pk)
    form = MatriculaForm(request.POST or None, instance = Matricula)
    if form.is_valid():
        form.save()
        return redirect('listar_matricula')
    return render(request, template_name, {'form':form})

def listar_cursturma(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cursoturma/listar_cursturma.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de curso turma',
            'cursturmas': Cursturma.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_cursturma(request, template_name='app/cursturma/novo_cursturma.html'):
    curso = Curso.objects.all()
    sigla_curso = request.POST.get('sigla_curso')
    disciplinofertada = Disciplinofertada.objects.all()
    nome_disciplina = request.POST.get('nome_disciplina')
    ano_disciplina = request.POST.get('ano_disciplina')
    semestre_disciplina = request.POST.get('semestre_disciplina')
    turma = Turma.objects.all()
    id_turma = request.POST.get('id_turma')
    form = CursturmaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_cursturma')
    return render(request, template_name, { 'form':form, 'curso': curso, 'disciplinofertada': disciplinofertada, 'turma': turma})


def apagar_cursturma(request, pk, template_name='app/cursturma/confirmacao_apagar_cursturma.html'):
    cursturma = get_object_or_404(Cursturma, pk=pk)
    if request.method=='POST':
        cursturma.delete()
        return redirect('listar_cursturma')
    return render(request, template_name, {'object':cursturma.sigla_curso})

def editar_cursturma(request, pk, template_name='app/cursturma/novo_cursturma.html'):
    if request.user.is_superuser:
        cursturma = get_object_or_404(Cursturma, pk=pk)
    else:
        cursturma = get_object_or_404(Cursturma, pk=pk)
    form = CursturmaForm(request.POST or None, instance = Cursturma)
    if form.is_valid():
        form.save()
        return redirect('listar_cursturma')
    return render(request, template_name, {'form':form})

def listar_questao(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/questao/listar_questao.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de questao',
            'questaos': Questao.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_questao(request, template_name='app/questao/novo_questao.html'):
    turma = Turma.objects.all()
    nome_disciplina = request.POST.get('nome_disciplina')
    ano_disciplina = request.POST.get('ano_disciplina')
    semestre_disciplina = request.POST.get('semestre_disciplina')
    id_turma = request.POST.get('id_turma')
    form = CursturmaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_questao')
    return render(request, template_name, { 'form':form, 'turma': turma})

def apagar_questao(request, pk, template_name='app/questao/confirmacao_apagar_questao.html'):
    questao = get_object_or_404(Questao, pk=pk)
    if request.method=='POST':
        questao.delete()
        return redirect('listar_questao')
    return render(request, template_name, {'object':questao.numero_questao})

def editar_questao(request, pk, template_name='app/questao/novo_questao.html'):
    if request.user.is_superuser:
        questao = get_object_or_404(Questao, pk=pk)
    else:
        questao = get_object_or_404(Questao, pk=pk)
    form = QuestaoForm(request.POST or None, instance = Questao)
    if form.is_valid():
        form.save()
        return redirect('listar_questao')
    return render(request, template_name, {'form':form})

def listar_resposta(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/resposta/listar_resposta.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de resposta',
            'respostas': Resposta.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_resposta(request, template_name='app/resposta/novo_resposta.html'):
    questao = Questao.objects.all()
    nome_disciplina = request.POST.get('nome_disciplina')
    ano_disciplina = request.POST.get('ano_disciplina')
    semestre_disciplina = request.POST.get('semestre_disciplina')
    id_turma = request.POST.get('id_turma')
    numero_questao = request.POST.get('numero_questao')
    aluno = Aluno.objects.all()
    ra_aluno = request.POST.get('ra_aluno')
    form = RespostaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_resposta')
    return render(request, template_name, { 'form':form, 'questao': questao, 'aluno': aluno})

def apagar_resposta(request, pk, template_name='app/resposta/confirmacao_apagar_resposta.html'):
    resposta = get_object_or_404(Resposta, pk=pk)
    if request.method=='POST':
        resposta.delete()
        return redirect('listar_resposta')
    return render(request, template_name, {'object':resposta.ra_aluno})

def editar_resposta(request, pk, template_name='app/resposta/novo_resposta.html'):
    if request.user.is_superuser:
        resposta = get_object_or_404(Resposta, pk=pk)
    else:
        resposta = get_object_or_404(Resposta, pk=pk)
    form = RespostaForm(request.POST or None, instance = Resposta)
    if form.is_valid():
        form.save()
        return redirect('listar_resposta')
    return render(request, template_name, {'form':form})

def listar_arquivresposta(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/arquivresposta/listar_arquivresposta.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de arquivo resposta',
            'arquivrespostas': Arquivresposta.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_arquivresposta(request, template_name='app/arquivresposta/novo_arquivresposta.html'):
    resposta = Resposta.objects.all()
    nome_disciplina = request.POST.get('nome_disciplina')
    ano_disciplina = request.POST.get('ano_disciplina')
    semestre_disciplina = request.POST.get('semestre_disciplina')
    id_turma = request.POST.get('id_turma')
    numero_questao = request.POST.get('numero_questao')
    aluno = Aluno.objects.all()
    ra_aluno = request.POST.get('ra_aluno')
    form = ArquivrespostaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_arquivresposta')
    return render(request, template_name, { 'form':form, 'resposta': resposta, 'aluno': aluno})

def apagar_arquivresposta(request, pk, template_name='app/arquivresposta/confirmacao_apagar_arquivresposta.html'):
    arquivresposta = get_object_or_404(Resposta, pk=pk)
    if request.method=='POST':
        arquivresposta.delete()
        return redirect('listar_arquivresposta')
    return render(request, template_name, {'object':arquivresposta.ra_aluno})

def editar_arquivresposta(request, pk, template_name='app/arquivresposta/novo_arquivresposta.html'):
    if request.user.is_superuser:
        arquivresposta = get_object_or_404(Arquivresposta, pk=pk)
    else:
        arquivresposta = get_object_or_404(Arquivresposta, pk=pk)
    form = ArquivrespostaForm(request.POST or None, instance = Arquivresposta)
    if form.is_valid():
        form.save()
        return redirect('listar_arquivresposta')
    return render(request, template_name, {'form':form})

def listar_arquivquestao(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/arquivquestao/listar_arquivquestao.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de arquivo questao',
            'arquivquestaos': Arquivquestao.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_arquivquestao(request, template_name='app/arquivquestao/novo_arquivquestao.html'):
    questao = Questao.objects.all()
    nome_disciplina = request.POST.get('nome_disciplina')
    ano_disciplina = request.POST.get('ano_disciplina')
    semestre_disciplina = request.POST.get('semestre_disciplina')
    id_turma = request.POST.get('id_turma')
    numero_questao = request.POST.get('numero_questao')
    form = ArquivquestaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_arquivquestao')
    return render(request, template_name, { 'form':form, 'questao': questao})

def apagar_arquivquestao(request, pk, template_name='app/arquivquestao/confirmacao_apagar_arquivquestao.html'):
    arquivquestao = get_object_or_404(Arquivquestao, pk=pk)
    if request.method=='POST':
        arquivquestao.delete()
        return redirect('listar_arquivquestao')
    return render(request, template_name, {'object':arquivquestao.numero_questao})

def editar_arquivquestao(request, pk, template_name='app/arquivquestao/novo_arquivquestao.html'):
    if request.user.is_superuser:
        arquivquestao = get_object_or_404(Arquivquestao, pk=pk)
    else:
        arquivquestao = get_object_or_404(Arquivquestao, pk=pk)
    form = ArquivquestaoForm(request.POST or None, instance = Arquivquestao)
    if form.is_valid():
        form.save()
        return redirect('listar_arquivquestao')
    return render(request, template_name, {'form':form})
