from datetime import datetime
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',

    url(r'^$', 'app.views.pagina_inicial', name='pagina_inicial'),

    url(r'^listar_aluno', 'app.views.listar_aluno', name='listar_aluno'),
    url(r'^novo_aluno', 'app.views.novo_aluno', name='novo_aluno'),
    url(r'^editar_aluno/(?P<pk>\d+)$', 'app.views.editar_aluno', name='editar_aluno'),
    url(r'^apagar_aluno/(?P<pk>\d+)$', 'app.views.apagar_aluno', name='apagar_aluno'),

    url(r'^listar_curso', 'app.views.listar_curso', name='listar_curso'),
    url(r'^novo_curso', 'app.views.novo_curso', name='novo_curso'),
    url(r'^editar_curso/(?P<pk>\d+)$', 'app.views.editar_curso', name='editar_curso'),
    url(r'^apagar_curso/(?P<pk>\d+)$', 'app.views.apagar_curso', name='apagar_curso'),

    url(r'^listar_disciplina', 'app.views.listar_disciplina', name='listar_disciplina'),
    url(r'^novo_disciplina', 'app.views.novo_disciplina', name='novo_disciplina'),
    url(r'^editar_disciplina/(?P<pk>\d+)$', 'app.views.editar_disciplina', name='editar_disciplina'),
    url(r'^apagar_disciplina/(?P<pk>\d+)$', 'app.views.apagar_disciplina', name='apagar_disciplina'),

    url(r'^listar_grade', 'app.views.listar_grade', name='listar_grade'),
    url(r'^novo_grade', 'app.views.novo_grade', name='novo_grade'),
    url(r'^editar_grade/(?P<pk>\d+)$', 'app.views.editar_disciplina', name='editar_grade'),
    url(r'^apagar_grade/(?P<pk>\d+)$', 'app.views.apagar_grade', name='apagar_grade'),

    url(r'^listar_periodo', 'app.views.listar_periodo', name='listar_periodo'),
    url(r'^novo_periodo', 'app.views.novo_periodo', name='novo_periodo'),
    url(r'^editar_periodo/(?P<pk>\d+)$', 'app.views.editar_periodo', name='editar_periodo'),
    url(r'^apagar_periodo/(?P<pk>\d+)$', 'app.views.apagar_periodo', name='apagar_periodo'),

    url(r'^listar_perioddisciplina', 'app.views.listar_perioddisciplina', name='listar_perioddisciplina'),
    url(r'^novo_perioddisciplina', 'app.views.novo_perioddisciplina', name='novo_perioddisciplina'),
    url(r'^editar_perioddisciplina/(?P<pk>\d+)$', 'app.views.editar_perioddisciplina', name='editar_perioddisciplina'),
    url(r'^apagar_perioddisciplina/(?P<pk>\d+)$', 'app.views.apagar_perioddisciplina', name='apagar_perioddisciplina'),

    url(r'^listar_professor', 'app.views.listar_professor', name='listar_professor'),
    url(r'^novo_professor', 'app.views.novo_professor', name='novo_professor'),
    url(r'^editar_professor/(?P<pk>\d+)$', 'app.views.editar_professor', name='editar_professor'),
    url(r'^apagar_professor/(?P<pk>\d+)$', 'app.views.apagar_professor', name='apagar_professor'),

)
