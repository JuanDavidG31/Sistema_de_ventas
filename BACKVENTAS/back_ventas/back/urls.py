# back/urls.py (Archivo Nuevo)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# El Router se encarga de crear todas las URLs del CRUD automáticamente
router = DefaultRouter()
router.register(r'departamentos', views.DepartamentoViewSet, basename='departamento')
router.register(r'municipios', views.MunicipioViewSet, basename='municipio')
router.register(r'lineas-producto', views.LineaProductoViewSet, basename='lineaproducto')
router.register(r'productos', views.ProductoViewSet, basename='producto')
router.register(r'clientes', views.ClienteViewSet, basename='cliente')
router.register(r'productos-imagenes', views.ProductoImagenViewSet, basename='productoimagen')
router.register(r'ventas', views.VentaViewSet, basename='venta')
router.register(r'ventas-detalles', views.VentaDetalleViewSet, basename='ventadetalle')
router.register(r'usuarios', views.UsuarioViewSet, basename='usuario')

# Las URLs de la API son generadas automáticamente por el router
urlpatterns = [
    path('', include(router.urls)),
]