from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=50)
    duracao = models.IntegerField()

    def __str__(self):
        return f"{self.nome}"


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="alunos")
    matricula = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f"{self.nome} {self.idade} anos ({self.matricula})"
