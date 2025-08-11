from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
    # Datos de ejemplo para productos (reemplazar con modelo real)
    productos = [
        {'nombre': 'Kit de Iluminación Profesional', 'precio': '89.99', 'imagen': 'iluminacion.jpg'},
        {'nombre': 'Micrófono de Estudio', 'precio': '59.99', 'imagen': 'microfono.jpg'},
        {'nombre': 'Software de Edición Premium', 'precio': '129.99', 'imagen': 'software.jpg'},
        {'nombre': 'Cámara 4K', 'precio': '299.99', 'imagen': 'camara.jpg'},
    ]

    return render(request, 'tienda/index.html', {
        'productos': productos,
        'carrito_count': 0  # Temporal hasta implementar carrito real
    })
