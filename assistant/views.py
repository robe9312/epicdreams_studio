import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')

        # Respuestas contextuales según el mensaje
        if 'hola' in user_message.lower() or 'saludos' in user_message.lower():
            response = "¡Hola! ¿En qué puedo ayudarte hoy? Puedes usar los botones de navegación para ir a cualquier sección."

        elif 'servicio' in user_message.lower():
            response = "Te redirijo a nuestros servicios creativos. ¡Tenemos soluciones increíbles para ti!"

        elif 'curso' in user_message.lower():
            response = "Descubre nuestros cursos especializados. ¿Qué te gustaría aprender hoy?"

        elif 'tienda' in user_message.lower() or 'comprar' in user_message.lower():
            response = "Explora nuestra tienda con productos exclusivos para creadores. ¡Encuentra herramientas increíbles!"

        elif 'contacto' in user_message.lower() or 'ayuda' in user_message.lower():
            response = "¿Necesitas ayuda directa? Te llevo a nuestro formulario de contacto."

        elif 'inicio' in user_message.lower() or 'principal' in user_message.lower():
            response = "Volvemos a la página principal. ¡Siempre es un buen lugar para comenzar!"

        else:
            response = "Puedo llevarte a: Servicios, Cursos, Tienda, Contacto o Inicio. ¿A dónde quieres ir?"

        return JsonResponse({'response': response})

    return JsonResponse({'error': 'Método no permitido'}, status=405)
