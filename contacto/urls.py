from django.urls import path
from . import views

app_name = 'contacto'  # Namespace para URLs

urlpatterns = [
    path('', views.index, name='index'),  # Vista principal de contacto
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),  # Para formulario
]
