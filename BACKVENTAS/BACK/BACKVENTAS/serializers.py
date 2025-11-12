from .models import ProductoImagen, Producto
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
   
    producto = serializers.IntegerField(
        write_only=True, 
        source='producto_id', 
        label="ID del Producto"
    )
    
    imagen_file = serializers.FileField(
        write_only=True, 
        required=True, 
        label="Archivo de Imagen a Subir"
    )
    
    imagen_url = serializers.URLField(read_only=True)
    
    class Meta:
        model = ProductoImagen
     
        fields = ['id', 'producto', 'imagen_url', 'imagen_file', 'producto_id']
        read_only_fields = ['producto_id'] 

    def create(self, validated_data):
        imagen_file = validated_data.pop('imagen_file')
        
        producto_id_int = validated_data.get('producto_id') 

        try:
            Producto.objects.using('default').get(id=producto_id_int)
        except Producto.DoesNotExist:
            raise serializers.ValidationError({"producto": f"El producto con ID {producto_id_int} no existe."})
        except Exception as e:
            raise serializers.ValidationError({"producto": f"Error al verificar el producto: {e}"})

       
        try:
             url_cloudinary = upload_to_cloudinary(imagen_file, producto_id_int)
        except Exception as e:
            raise serializers.ValidationError({"imagen_file": f"Error al subir a Cloudinary: {e}"})

        validated_data['imagen_url'] = url_cloudinary
        
        
        producto_imagen = ProductoImagen.objects.using('mongo_db').create(**validated_data)
        
        return producto_imagen

class ProductoSerializer(serializers.ModelSerializer):
  
    imagenes = serializers.SerializerMethodField() 
    
    class Meta:
        model = Producto
        fields = '__all__'

    def get_imagenes(self, obj):
        
        imagenes_qs = ProductoImagen.objects.using('mongo_db').filter(producto_id=obj.id)
        
   
        return ProductoImagenSerializer(imagenes_qs, many=True, read_only=True, context=self.context).data

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