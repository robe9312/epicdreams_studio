from django.urls import path
from . import views

app_name = 'servicios'  # Namespace para URLs

urlpatterns = [
    path('', views.index, name='index'),  # Vista principal
]
