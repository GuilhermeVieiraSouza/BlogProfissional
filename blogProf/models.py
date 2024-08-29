from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='cursos', null=True, blank=True)

    def __str__(self):
        return self.nome

class Guilherme(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='Guilherme', null=True, blank=True)
    cursos = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome