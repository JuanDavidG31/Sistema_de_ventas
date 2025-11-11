
from django.contrib.auth.models import User # Importamos el User nativo de Django
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
    # Campo 'password' para recibir la contraseña en texto plano, solo para escribir
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Usuario
        # Añadir 'password' a los campos
        fields = ['id', 'username', 'email', 'rol', 'nombre_completo', 'password']
        
    def create(self, validated_data):
        # 1. Extraer la contraseña y el nombre de usuario
        password = validated_data.pop('password')
        username = validated_data['username']
        email = validated_data['email']
        
        # 2. Crear el objeto Usuario personalizado (BACKVENTAS.Usuario)
        # La contraseña hasheada la guarda el modelo User de Django
        usuario_custom = Usuario.objects.create(**validated_data)
        
        # 3. Crear el objeto User nativo de Django para la autenticación
        # Usamos create_user para hashear la contraseña automáticamente
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        return usuario_custom

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