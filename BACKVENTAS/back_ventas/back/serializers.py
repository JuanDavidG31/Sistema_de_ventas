

from rest_framework import serializers
from .models import (
    Departamento, Municipio, LineaProducto, Producto, 
    Cliente, ProductoImagen, Venta, VentaDetalle, Usuario
)



class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'  # '__all__' significa que incluye todos los campos del modelo

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'

class LineaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineaProducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProductoImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoImagen
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


# --- Serializers para Transacciones (Ventas) ---
# (Estos pueden ser más complejos luego, pero para un CRUD básico empezamos así)

class VentaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaDetalle
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    # Opcional: Si quieres ver los detalles DENTRO de la venta
    # detalles = VentaDetalleSerializer(many=True, read_only=True) 
    
    class Meta:
        model = Venta
        fields = '__all__'
        # Si usas el opcional de arriba, añade 'detalles' a los fields