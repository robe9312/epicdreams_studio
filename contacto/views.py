from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ContactoForm  # Crearemos este formulario después

@login_required(login_url='/accounts/login/')
def index(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # En una implementación real, aquí enviaríamos el email
            messages.success(request, '¡Mensaje enviado con éxito! Te responderemos pronto.')
            return redirect('contacto:index')
    else:
        # Prellenar con datos del usuario si está autenticado
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'nombre': request.user.get_full_name(),
                'email': request.user.email
            }
        form = ContactoForm(initial=initial_data)

    return render(request, 'contacto/index.html', {'form': form})

def enviar_mensaje(request):
    # Esta función se implementará cuando tengamos el formulario
    pass
