from rest_framework.permissions import IsAuthenticated, AllowAny # 🚨 ¡Faltaba importar AllowAny!

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
    permission_classes = [permissions.IsAuthenticated]

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    permission_classes = [permissions.IsAuthenticated]

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    # Sobreescribir el método get_permissions para aplicar reglas diferentes por acción
    def get_permissions(self):
        """
        Instancia y devuelve la lista de permisos que esta vista requiere.
        """
        # Si la acción es 'create' (POST /api/usuarios/), permitir acceso público (AllowAny)
        if self.action == 'create':
            permission_classes = [AllowAny]
        # Para todas las demás acciones (list, retrieve, update, destroy), requerir autenticación
        else:
            permission_classes = [IsAuthenticated]
            
        return [permission() for permission in permission_classes]
# --- ViewSets de Clientes y Productos ---

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

class LineaProductoViewSet(viewsets.ModelViewSet):
    queryset = LineaProducto.objects.all()
    serializer_class = LineaProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductoImagenViewSet(viewsets.ModelViewSet):
    queryset = ProductoImagen.objects.all()
    serializer_class = ProductoImagenSerializer
    permission_classes = [permissions.IsAuthenticated]

# --- ViewSets de Venta ---

class VentaDetalleViewSet(viewsets.ModelViewSet):
    queryset = VentaDetalle.objects.all()
    serializer_class = VentaDetalleSerializer
    permission_classes = [permissions.IsAuthenticated]

class VentaViewSet(viewsets.ModelViewSet):
    
    queryset = Venta.objects.prefetch_related('detalles').all()
    serializer_class = VentaSerializer
    permission_classes = [permissions.IsAuthenticated]