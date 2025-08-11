#!/bin/bash

# Activar entorno virtual (ajusta si tu entorno se llama diferente)
source env/bin/activate

# Ejecutar servidor Django en background
python manage.py runserver &

# Guardar el PID del servidor para poder manejarlo si quieres (opcional)
SERVER_PID=$!

# Esperar 3 segundos a que el servidor arranque
sleep 3

# Abrir navegador en localhost:8000 (puerto por defecto)
xdg-open http://127.0.0.1:8000/

# Esperar hasta que el servidor se cierre (opcional)
wait $SERVER_PID
