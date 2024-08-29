from django.shortcuts import render
from .models import Guilherme

# Create your views here.
def home(request):
    guilherme = Guilherme.objects.all()
    context = {
        'guilhermes': guilherme
    }
    print(guilherme)
    return render(request, 'blogProf/home.html', context)

def detalhe(request):
    eu = Guilherme.objects.all()
    return render(request, 'detalhe.html')