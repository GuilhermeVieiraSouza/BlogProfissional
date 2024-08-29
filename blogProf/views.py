from django.shortcuts import render
from .models import Eu

# Create your views here.
def home(request):
    eu = Eu.objects.all()
    return render(request, 'blogProf/home.html', {'eu': eu})

def detalhe(request):
    eu = Eu.objects.all()
    return render(request, 'detalhe.html')