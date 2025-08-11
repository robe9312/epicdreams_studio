from django.urls import path
from . import views

app_name = 'core'  # Namespace para URLs

urlpatterns = [
    path('', views.index, name='index'),  # Usar 'index' en lugar de 'home'
]
