# urls.py (Archivo principal, el que subiste)
from django.contrib import admin
from django.urls import path, include, re_path # Importamos re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Importaciones para drf-yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# 1. Definición del Esquema
schema_view = get_schema_view(
   openapi.Info(
      title="API BACKVENTAS",
      default_version='v1',
      description="Documentación de la API de Gestión de Ventas.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contacto@ejemplo.com"),
      license=openapi.License(name="Licencia BSD"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


# 2. Definición de URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('BACKVENTAS.urls')),

    # Endpoints JWT (autenticación)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Rutas para Swagger (Documentación)
    # Ruta para el JSON o YAML del esquema (el documento base)
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    
    # *** ESTA ES LA URL PARA ABRIR SWAGGER ***
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # Ruta alternativa de documentación (Redoc)
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]