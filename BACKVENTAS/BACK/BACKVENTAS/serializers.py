
from .utils import upload_to_cloudinary
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
    
    imagen_file = serializers.FileField(
        write_only=True, 
        required=True, 
        label="Archivo de Imagen a Subir"
    )
    
    
    imagen_url = serializers.URLField(read_only=True)
    
    class Meta:
        model = ProductoImagen
       
        fields = ['id', 'producto', 'imagen_url', 'imagen_file']
        
    def create(self, validated_data):
        imagen_file = validated_data.pop('imagen_file')
        
        producto_instance = validated_data['producto']
        
     
        try:
            url_cloudinary = upload_to_cloudinary(imagen_file, producto_instance.id)
        except Exception as e:
            raise serializers.ValidationError(f"Error al subir a Cloudinary: {e}")

     
        validated_data['imagen_url'] = url_cloudinary
        
        
        producto_imagen = ProductoImagen.objects.create(**validated_data)
        
        return producto_imagen

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