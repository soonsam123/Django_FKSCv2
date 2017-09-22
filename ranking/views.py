from django.views import generic
from .models import Rank_campeonato

class IndexView(generic.ListView):
    template_name = 'ranking/index.html'
    context_object_name = 'todos_campeonatos'

    def get_queryset(self):
        return Rank_campeonato.objects.all()

class DetailView(generic.DetailView):
    model = Rank_campeonato
    template_name = 'ranking/detail.html'
