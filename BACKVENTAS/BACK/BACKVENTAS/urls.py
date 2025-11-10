

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



router = DefaultRouter()


router.register(r'departamentos', DepartamentoViewSet, basename='departamentos')
router.register(r'municipios', MunicipioViewSet, basename='municipios')
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'clientes', ClienteViewSet, basename='clientes')
router.register(r'lineasproducto', LineaProductoViewSet, basename='lineasproducto')
router.register(r'productos', ProductoViewSet, basename='productos')
router.register(r'productoimagenes', ProductoImagenViewSet, basename='productoimagenes')
router.register(r'ventas', VentaViewSet, basename='ventas')
router.register(r'ventadetalles', VentaDetalleViewSet, basename='ventadetalles')



urlpatterns = router.urls