from urllib import response
from .utils import delete_from_cloudinary
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser
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
from rest_framework import status
from rest_framework.response import Response
from bson.objectid import ObjectId
from django.shortcuts import get_object_or_404

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
    lookup_field = '_id'
    parser_classes = (MultiPartParser, FormParser,) 
    
  
    @swagger_auto_schema(
        operation_description="Sube una imagen para un producto específico.",
        request_body=ProductoImagenSerializer, 
        consumes=['multipart/form-data'] 
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    #permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        lookup_value = self.kwargs[self.lookup_field] 
        
        try:
            object_id = ObjectId(lookup_value)
        except Exception:
            raise status.HTTP_404_NOT_FOUND("ID de Objeto no válido.") 

        
        filter_kwargs = {self.lookup_field: object_id}
        
        return get_object_or_404(self.get_queryset(), **filter_kwargs)
    def destroy(self, request, *args, **kwargs):
       
        try:
           
            instance = self.get_object() 
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND) 

        
        imagen_url = instance.imagen_url
        self.perform_destroy(instance)
        
        from .utils import delete_from_cloudinary
        if delete_from_cloudinary(imagen_url):
            print(f"Imagen {imagen_url} eliminada exitosamente de Cloudinary.")
        else:
            print(f"ATENCIÓN: Fallo al eliminar {imagen_url} de Cloudinary.")
            
        return Response(status=status.HTTP_204_NO_CONTENT)

# --- ViewSets de Venta ---

class VentaDetalleViewSet(viewsets.ModelViewSet):
    queryset = VentaDetalle.objects.all()
    serializer_class = VentaDetalleSerializer
    #permission_classes = [permissions.IsAuthenticated]

class VentaViewSet(viewsets.ModelViewSet):
    
    queryset = Venta.objects.prefetch_related('detalles').all()
    serializer_class = VentaSerializer
    #permission_classes = [permissions.IsAuthenticated]