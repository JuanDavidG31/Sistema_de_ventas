

from rest_framework import serializers
from .models import (
    Departamento, Municipio, Usuario, Cliente, LineaProducto, 
    Producto, ProductoImagen, Venta, VentaDetalle
)

# --- Serializers de Localización y Usuarios ---

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        
        fields = ['id', 'username', 'email', 'rol', 'nombre_completo'] 

# --- Serializers de Clientes y Productos ---

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class LineaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineaProducto
        fields = '__all__'

class ProductoImagenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductoImagen
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
  
    imagenes = ProductoImagenSerializer(many=True, read_only=True) 
    class Meta:
        model = Producto
        fields = '__all__'

# --- Serializers de Venta ---

class VentaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaDetalle
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    
    detalles = VentaDetalleSerializer(many=True, read_only=True) 
    class Meta:
        model = Venta
        fields = '__all__'