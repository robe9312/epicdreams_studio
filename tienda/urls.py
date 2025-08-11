from django.urls import path
from . import views

app_name = 'tienda'  # Namespace para URLs

urlpatterns = [
    path('', views.index, name='index'),  # Vista principal de tienda
]
