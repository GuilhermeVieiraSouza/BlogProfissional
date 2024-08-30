from django.db import models

class Habilidades(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome

class Atividades(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome

class Pessoal(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagemIntro = models.ImageField(upload_to='media/', blank=True)
    imagemBg = models.ImageField(upload_to='media/', blank=True)
    imagem = models.ImageField(upload_to='media/', blank=True)
    video = models.FileField(upload_to='videos/', blank=True)
    portfolio = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return self.titulo