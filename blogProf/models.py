from django.db import models

# Create your models here.

class Eu(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='eu', null=True, blank=True)

    def __str__(self):
        return self.nome