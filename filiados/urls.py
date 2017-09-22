from django.conf.urls import url
from . import views

app_name = 'filiados'

urlpatterns = [
    # /filiados/
    url(r'^$', views.index, name='index'),

    # /filiados/academias/
    url(r'^academias/$', views.academias, name='academias'),

    # /filiados/atletas/
    url(r'^atletas/$', views.atletas, name='atletas'),

    # /filiados/pretas/
    url(r'^pretas/$', views.pretas, name='pretas'),
]

