from django.shortcuts import render
#Importamos los modelos
from .models import Project
# Create your views here.


def home(request):
    proyectos = Project.objects.all()

    return render(request, 'home.html', {'proyectos': proyectos})