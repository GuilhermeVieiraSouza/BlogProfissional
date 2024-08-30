from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('index/', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('academico/', views.academico, name='academico'),
    path('pessoal/', views.pessoal, name='pessoal'),
    
    
] 

