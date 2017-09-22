from .models import Academia, Atleta, Preta
from django.shortcuts import render

def index(request):
    return render(request, 'inicial/index.html')

def ordenar_num(lista):
    for i in range(0,len(lista)):
        for j in range(i,len(lista)):
            if lista[i] >= lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

def ordenar(todas_academias):
    lista = []
    for academia in todas_academias:
        lista = lista + [academia.num_reg]
    num_organizados = ordenar_num(lista)
    nova_lista_academias = []
    for reg in num_organizados:
        for academia in todas_academias:
            if reg == academia.num_reg:
                nova_lista_academias = nova_lista_academias + [academia]
    return nova_lista_academias

def academias(request):
    todas_academias = Academia.objects.all()
    return render(request,'filiados/academias.html', {'todas_academias': ordenar(todas_academias)})

def atletas(request):
    todos_atletas = Atleta.objects.all()
    return render(request, 'filiados/atletas.html', {'todos_atletas': ordenar(todos_atletas)})

def pretas(request):
    todos_pretas = Preta.objects.all()
    return render(request, 'filiados/pretas.html', {'todos_pretas': ordenar(todos_pretas)})