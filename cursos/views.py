from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Curso  # Importación del modelo Curso

# Vista para la página principal
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'cursos/index.html')

# Vista para el detalle de cursos
@login_required(login_url='/accounts/login/')
def curso_detalle(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    contexto = {
        'curso': curso,
        'usuario': request.user,
    }

    return render(request, 'cursos/curso_detalle.html', contexto)
