from django.shortcuts import render
from django.views import generic
from .models import Campeonato

class IndexView(generic.ListView):
    template_name = 'campeonatos/index.html'
    context_object_name = 'todos_campeonatos'

    def get_queryset(self):
        return Campeonato.objects.all()

