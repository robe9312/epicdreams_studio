from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
    # Datos de ejemplo para servicios (reemplazar con modelo real)
    servicios = [
        {'nombre': 'Producción Audiovisual', 'descripcion': 'Creación de contenido cinematográfico profesional'},
        {'nombre': 'Diseño Gráfico', 'descripcion': 'Soluciones visuales para tu marca'},
        {'nombre': 'Consultoría Creativa', 'descripcion': 'Asesoramiento especializado para proyectos artísticos'},
    ]

    return render(request, 'servicios/index.html', {'servicios': servicios})
