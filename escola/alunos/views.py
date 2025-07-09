from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import models
# Create your views here.
def lista_alunos(request):
    alunos = models.Aluno.objects.all()
    cursos = models.Curso.objects.all()
    return render(request, 'alunos/lista.html', {'alunos' : alunos , 'cursos' : cursos})

def matricular(request):
    if request.method == "POST":
        nome = models.Aluno(nome=request.POST["nome"],curso=models.Curso.objects.get(nome = request.POST["curso"]),idade=request.POST["idade"])
        nome.save()
        return HttpResponseRedirect(reverse("lista_alunos"))
    alunos = models.Aluno.objects.all()
    cursos = models.Curso.objects.all()
    return render(request, 'alunos/matricula.html', {'alunos' : alunos , 'cursos' : cursos})