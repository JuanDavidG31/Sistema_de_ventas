"""
URL configuration for back_ventas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# back_ventas/urls.py (Modificado)

from django.contrib import admin
from django.urls import path, include  # <-- Asegúrate de importar 'include'

# --- 1. Importaciones para drf-yasg (Swagger) ---
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# --- 2. Configuración de la vista de Swagger ---
schema_view = get_schema_view(
   openapi.Info(
      title="API Ventas Juguetes (BackVentas)",
      default_version='v1',
      description="Documentación oficial de la API para el sistema de ventas de juguetes.",
      contact=openapi.Contact(email="tu_email@proyecto.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,), # Permite que cualquiera vea la doc
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- 3. URL de tu API ---
    # Todas las URLs de tu app 'back' estarán bajo 'api/v1/'
    # Ejemplo: /api/v1/productos/
    # Ejemplo: /api/v1/clientes/
    path('api/v1/', include('back.urls')), 
    
    # --- 4. URLs de la documentación ---
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
