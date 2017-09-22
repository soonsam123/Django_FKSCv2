from django.views import generic
from .models import Convocado_campeonato

class IndexView(generic.ListView):
    template_name = 'convocados/index.html'
    context_object_name = 'todos_campeonatos'

    def get_queryset(self):
        return Convocado_campeonato.objects.all()

class DetailView(generic.DetailView):
    model = Convocado_campeonato
    template_name = 'convocados/detail.html'
