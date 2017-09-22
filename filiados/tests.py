from django.test import TestCase

class IndexView(generic.ListView):
    template_name = 'filiados/index.html'
    context_object_name = 'todas_academias'

    def get_queryset(self):
        return Academia.objects.all()