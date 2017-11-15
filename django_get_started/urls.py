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

    url(r'^listar_matricula', 'app.views.listar_matricula', name='listar_matricula'),
    url(r'^novo_matricula', 'app.views.novo_matricula', name='novo_matricula'),
    url(r'^editar_matricula/(?P<pk>\d+)$', 'app.views.editar_matricula', name='editar_matricula'),
    url(r'^apagar_matricula/(?P<pk>\d+)$', 'app.views.apagar_matricula', name='apagar_matricula'),

    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

)
