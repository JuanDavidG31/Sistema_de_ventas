# BACKVENTAS/urls.py

from rest_framework.routers import DefaultRouter
from .views import (
    DepartamentoViewSet, 
    MunicipioViewSet, 
    UsuarioViewSet, 
    ClienteViewSet, 
    LineaProductoViewSet, 
    ProductoViewSet, 
    ProductoImagenViewSet, 
    VentaViewSet, 
    VentaDetalleViewSet
)

# Creamos una instancia de DefaultRouter. 
# Esto genera automáticamente las rutas para Listar, Crear, Obtener, Actualizar y Eliminar (CRUD)
router = DefaultRouter()

# Registra cada ViewSet con su respectivo prefijo de URL
# Por ejemplo: 'productos/' para ProductoViewSet.
router.register(r'departamentos', DepartamentoViewSet, basename='departamentos')
router.register(r'municipios', MunicipioViewSet, basename='municipios')
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'clientes', ClienteViewSet, basename='clientes')
router.register(r'lineasproducto', LineaProductoViewSet, basename='lineasproducto')
router.register(r'productos', ProductoViewSet, basename='productos')
router.register(r'productoimagenes', ProductoImagenViewSet, basename='productoimagenes')
router.register(r'ventas', VentaViewSet, basename='ventas')
router.register(r'ventadetalles', VentaDetalleViewSet, basename='ventadetalles')


# El patrón de URLs final que incluye todas las rutas generadas por el router
urlpatterns = router.urls