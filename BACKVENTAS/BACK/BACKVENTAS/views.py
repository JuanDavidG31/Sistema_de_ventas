

from rest_framework import viewsets, permissions
from .models import (
    Departamento, Municipio, Usuario, Cliente, LineaProducto, 
    Producto, ProductoImagen, Venta, VentaDetalle
)
from .serializers import (
    DepartamentoSerializer, MunicipioSerializer, UsuarioSerializer, ClienteSerializer, 
    LineaProductoSerializer, ProductoSerializer, ProductoImagenSerializer, 
    VentaSerializer, VentaDetalleSerializer
)

# --- ViewSets de Localización y Usuarios ---

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    #permission_classes = [permissions.IsAuthenticated]

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    #permission_classes = [permissions.IsAuthenticated]

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #permission_classes = [permissions.IsAuthenticated]

# --- ViewSets de Clientes y Productos ---

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #permission_classes = [permissions.IsAuthenticated]

class LineaProductoViewSet(viewsets.ModelViewSet):
    queryset = LineaProducto.objects.all()
    serializer_class = LineaProductoSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ProductoImagenViewSet(viewsets.ModelViewSet):
    queryset = ProductoImagen.objects.using('mongo_db').all()
    serializer_class = ProductoImagenSerializer
    #permission_classes = [permissions.IsAuthenticated]

# --- ViewSets de Venta ---

class VentaDetalleViewSet(viewsets.ModelViewSet):
    queryset = VentaDetalle.objects.all()
    serializer_class = VentaDetalleSerializer
    #permission_classes = [permissions.IsAuthenticated]

class VentaViewSet(viewsets.ModelViewSet):
    
    queryset = Venta.objects.prefetch_related('detalles').all()
    serializer_class = VentaSerializer
    #permission_classes = [permissions.IsAuthenticated]