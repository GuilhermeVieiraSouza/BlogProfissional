from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    pessoal = Pessoal.objects.all().first()
    contexto = {
        'pessoal': pessoal,
    }
    return render(request, 'blogProf/home.html', contexto)

def sobre(request):
    pessoal = Pessoal.objects.all().first()
    contexto = {
        'pessoal': pessoal,
    }
    return render(request, 'blogProf/sobre.html', contexto)

def academico(request):
    habilidades = Habilidades.objects.all()
    atividades = Atividades.objects.all()
    pessoal = Pessoal.objects.all().first()
    contexto = {
        'lista': habilidades,
        'cursos': atividades,
        'pessoal': pessoal,
    }
    return render(request, 'blogProf/academico.html', contexto)

def pessoal(request):
    publicacao = Pessoal.objects.all()
    contexto = {
        'posts': publicacao,
    }

    return render(request, 'blogProf/pessoal.html', contexto)