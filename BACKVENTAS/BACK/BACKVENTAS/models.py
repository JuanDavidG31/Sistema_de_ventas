from django.db import models
from django.contrib.postgres.fields import JSONField  
from django.utils import timezone

class Departamento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    codigo = models.CharField(max_length=10, unique=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, related_name='municipios')
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} - {self.departamento.nombre}"

class Usuario(models.Model):
    ROLE_CHOICES = (('ADMIN','ADMIN'), ('VENDEDOR','VENDEDOR'), ('CONTADOR','CONTADOR'))
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128)  
    rol = models.CharField(max_length=10, choices=ROLE_CHOICES)
    nombre_completo = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Cliente(models.Model):
    TIPO_PAGO_CHOICES = (('CONTADO','Contado'), ('CREDITO','Crédito'), ('MIXTO','Mixto'))
    ESTADO_CHOICES = (('ACTIVO','Activo'), ('INACTIVO','Inactivo'))

    nombre = models.CharField(max_length=200)
    tipo_documento = models.CharField(max_length=4)
    documento = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, related_name='clientes')
    tipo_pago = models.CharField(max_length=10, choices=TIPO_PAGO_CHOICES)
    credito_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)

    def __str__(self):
        return f"{self.nombre} ({self.documento})"

class LineaProducto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    linea = models.ForeignKey(LineaProducto, on_delete=models.PROTECT, related_name='productos')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    iva_porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    stock_total = models.IntegerField()
    estado = models.CharField(max_length=10)
    sku = models.CharField(max_length=50, blank=True, null=True)
    opciones = models.JSONField(default=dict, blank=True)  

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
    url_almacenamiento = models.URLField()
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"Imagen {self.id} - {self.producto.codigo}"

class Venta(models.Model):
    numero_factura = models.CharField(max_length=50, unique=True)
    fecha_hora = models.DateTimeField(default=timezone.now)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='ventas')
    forma_pago = models.CharField(max_length=10)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    total_iva = models.DecimalField(max_digits=10, decimal_places=2)
    total_general = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10)
    usuario_vendedor = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='ventas')

    def __str__(self):
        return self.numero_factura

class VentaDetalle(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, related_name='detalles_venta')
    codigo_producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje_iva = models.DecimalField(max_digits=5, decimal_places=2)
    valor_sin_iva = models.DecimalField(max_digits=10, decimal_places=2)
    valor_iva = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('venta', 'producto')  

    def __str__(self):
        return f"{self.venta.numero_factura} - {self.producto.codigo}"
