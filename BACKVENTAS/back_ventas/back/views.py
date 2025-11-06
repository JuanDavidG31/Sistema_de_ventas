from django.shortcuts import render


from rest_framework import viewsets
# Importa todos tus modelos y serializers
from .models import (
    Departamento, Municipio, LineaProducto, Producto, 
    Cliente, ProductoImagen, Venta, VentaDetalle, Usuario
)
from .serializers import (
    DepartamentoSerializer, MunicipioSerializer, LineaProductoSerializer, 
    ProductoSerializer, ClienteSerializer, ProductoImagenSerializer, 
    VentaSerializer, VentaDetalleSerializer, UsuarioSerializer
)

# --- ViewSets para la API ---

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class LineaProductoViewSet(viewsets.ModelViewSet):
    queryset = LineaProducto.objects.all()
    serializer_class = LineaProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProductoImagenViewSet(viewsets.ModelViewSet):
    queryset = ProductoImagen.objects.all()
    serializer_class = ProductoImagenSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VentaDetalleViewSet(viewsets.ModelViewSet):
    queryset = VentaDetalle.objects.all()
    serializer_class = VentaDetalleSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer