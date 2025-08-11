# /home/robe/epicdreams_web/config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
# Añadir estas importaciones
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('assistant/', include(('assistant.urls', 'assistant'), namespace='assistant')),
    path('servicios/', include(('servicios.urls', 'servicios'), namespace='servicios')),
    path('cursos/', include(('cursos.urls', 'cursos'), namespace='cursos')),
    path('tienda/', include(('tienda.urls', 'tienda'), namespace='tienda')),
    path('contacto/', include(('contacto.urls', 'contacto'), namespace='contacto')),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(next_page='/'),
         name='logout'),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('favicon.ico')
    )),
]

# AÑADIR ESTO AL FINAL DEL ARCHIVO
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
