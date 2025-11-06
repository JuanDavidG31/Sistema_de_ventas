from django.db import models
from django.core.validators import MinValueValidator

# --- Choices Fijos ---
TIPO_PAGO_CHOICES = [
    ('CONTADO', 'Contado'),
    ('CREDITO', 'Crédito'),
    ('MIXTO', 'Mixto'),
]
ESTADO_ACTIVO_CHOICES = [
    ('ACTIVO', 'Activo'),
    ('INACTIVO', 'Inactivo'),
]
TIPO_DOCUMENTO_CHOICES = [
    ('CC', 'Cédula de Ciudadanía'),
    ('NIT', 'Número de Identificación Tributaria'),
    ('OTRO', 'Otro Documento'),
]
FORMA_PAGO_VENTA_CHOICES = [
    ('CONTADO', 'Contado'),
    ('CREDITO', 'Crédito'),
]
ESTADO_VENTA_CHOICES = [
    ('COMPLETA', 'Completa'),
    ('ANULADA', 'Anulada'),
    ('PENDIENTE', 'Pendiente'),
]
ROL_USUARIO_CHOICES = [
    ('ADMIN', 'Administrador'),
    ('VENDEDOR', 'Vendedor'),
    ('CONTADOR', 'Contador'),
]


# --- 1. Modelos de Ubicación ---

class Departamento(models.Model):
    # id_departamento PK (se crea automáticamente como 'id')
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Departamento")
    codigo = models.CharField(max_length=10, unique=True, verbose_name="Código Dpto")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'departamento'

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    # id_municipio PK (se crea automáticamente como 'id')
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Municipio")
    codigo = models.CharField(max_length=10, unique=True, verbose_name="Código Mpio")
    
    # FK -> DEPARTAMENTO (Relación 1 a N)
    departamento = models.ForeignKey(
        Departamento, 
        on_delete=models.PROTECT, # No permite borrar el depto si tiene municipios
        verbose_name="Departamento"
    )
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'municipio' 

    def __str__(self):
        return f"{self.nombre} ({self.departamento.nombre})"

# --- 2. Modelos de Clientes y Usuarios ---

class Usuario(models.Model):
    # id_usuario PK (se crea automáticamente como 'id')
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128, verbose_name="Hash de Contraseña") 
    rol = models.CharField(max_length=10, choices=ROL_USUARIO_CHOICES, default='VENDEDOR')
    nombre_completo = models.CharField(max_length=255)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.nombre_completo


class Cliente(models.Model):
    # id_cliente PK (se crea automáticamente como 'id')
    nombre = models.CharField(max_length=200)
    
    # Nuevos campos del esquema detallado
    tipo_documento = models.CharField(max_length=4, choices=TIPO_DOCUMENTO_CHOICES, default='CC') 
    
    # ********************************
    # ¡LA CORRECCIÓN ESTÁ AQUÍ!
    # ********************************
    documento = models.CharField(
        max_length=20, 
        unique=True, 
        blank=True,  # Permite que el campo esté vacío en el formulario/API
        null=True,   # Permite almacenar NULL en la DB (Soluciona el error 11000 de Mongo)
        verbose_name="Documento/NIT"
    ) 
    
    correo = models.EmailField(blank=True, null=True, verbose_name="Correo") 
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    
    # FK -> MUNICIPIO (Relación 1 a N)
    id_municipio = models.ForeignKey(
        Municipio, 
        on_delete=models.PROTECT, 
        verbose_name="Municipio"
    )
    
    tipo_pago = models.CharField(max_length=10, choices=TIPO_PAGO_CHOICES, default='CONTADO')
    credito_maximo = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00, 
        validators=[MinValueValidator(0)]
    )
    estado = models.CharField(max_length=10, choices=ESTADO_ACTIVO_CHOICES, default='ACTIVO')

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return f"{self.nombre} ({self.documento})"


# --- 3. Modelos de Productos ---

class LineaProducto(models.Model):
    # id_linea PK (se crea automáticamente como 'id')
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de Línea")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    
    class Meta:
        db_table = 'linea_producto'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    # id_producto PK (se crea automáticamente como 'id')
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código de Producto")
    nombre = models.CharField(max_length=255, verbose_name="Nombre del Producto")
    descripcion = models.TextField(blank=True, null=True)
    
    # FK -> LINEA_PRODUCTO (Relación 1 a N)
    id_linea = models.ForeignKey(
        LineaProducto, 
        on_delete=models.PROTECT, 
        verbose_name="Línea de Producto"
    )
    
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    # Nuevo campo del esquema
    iva_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, validators=[MinValueValidator(0)]) 
    # De 'stock' a 'stock_total'
    stock_total = models.IntegerField(default=0, blank=True, null=True) 
    estado = models.CharField(max_length=10, choices=ESTADO_ACTIVO_CHOICES, default='ACTIVO')
    sku = models.CharField(max_length=50, blank=True, null=True)
    # Nuevo campo JSON
    opciones = models.JSONField(blank=True, null=True, default=dict, verbose_name="Atributos Extensibles (JSON)") 

    class Meta:
        db_table = 'producto'

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

class ProductoImagen(models.Model):
    # id_imagen PK (se crea automáticamente como 'id')
    # FK -> PRODUCTO (Relación 1 a N)
    id_producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE, # Si se borra el producto, borra la imagen
        related_name='imagenes', 
        verbose_name="Producto"
    )
    
    url_almacenamiento = models.URLField(max_length=500)
    # Nuevo campo JSON para NoSQL/Metadatos
    metadata = models.JSONField(
        blank=True, 
        null=True, 
        default=dict,
        verbose_name="Tags, Variante, Metadata, etc."
    )
    # Se eliminó 'es_principal' para usar el campo 'metadata' si es necesario.

    class Meta:
        db_table = 'producto_imagen'

    def __str__(self):
        return f"Imagen de {self.id_producto.nombre}"

# --- 4. Modelos de Ventas (Transacciones) ---

class Venta(models.Model):
    # id_venta PK (se crea automáticamente como 'id')
    numero_factura = models.CharField(max_length=50, unique=True, verbose_name="Número de Factura")
    fecha_hora = models.DateTimeField(auto_now_add=True)
    
    # FK -> CLIENTE
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name="Cliente")
    
    forma_pago = models.CharField(max_length=10, choices=FORMA_PAGO_VENTA_CHOICES, default='CONTADO')
    # Nuevos campos calculados
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])
    total_iva = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])
    total_general = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])
    
    estado = models.CharField(max_length=10, choices=ESTADO_VENTA_CHOICES, default='PENDIENTE')
    
    # FK -> USUARIO
    usuario_vendedor = models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name="Vendedor")

    class Meta:
        db_table = 'venta'

    def __str__(self):
        return f"Factura N° {self.numero_factura}"


class VentaDetalle(models.Model):
    # id_detalle PK (se crea automáticamente como 'id')
    
    # FK -> VENTA
    id_venta = models.ForeignKey(
        Venta, 
        on_delete=models.CASCADE, 
        related_name='detalles', # Permite acceder a los detalles desde la Venta: venta.detalles.all()
        verbose_name="Venta"
    )
    
    # FK -> PRODUCTO
    id_producto = models.ForeignKey(
        Producto, 
        on_delete=models.PROTECT, 
        verbose_name="Producto"
    )
    
    codigo_producto = models.CharField(max_length=50, verbose_name="Código del Producto (Audit)") # Redundante
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje_iva = models.DecimalField(max_digits=5, decimal_places=2)
    
    # Nuevos campos calculados
    valor_sin_iva = models.DecimalField(max_digits=10, decimal_places=2)
    valor_iva = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'venta_detalle'
        unique_together = ('id_venta', 'id_producto') 

    def __str__(self):
        return f"{self.cantidad} x {self.id_producto.nombre} en Factura {self.id_venta.numero_factura}"