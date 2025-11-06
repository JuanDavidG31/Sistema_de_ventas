# back/models.py

from django.db import models

# --- 1. Modelos de Ubicación (Tablas Maestras) ---

class Departamento(models.Model):
    # El campo _id (clave primaria en MongoDB) es añadido automáticamente por Djongo
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Departamento")
    codigo = models.CharField(max_length=10, unique=True, verbose_name="Código Dpto")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        # Djongo usa este nombre para la colección en MongoDB
        db_table = 'departamento' 

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Municipio")
    codigo = models.CharField(max_length=10, unique=True, verbose_name="Código Mpio")
    # Relación ForeignKey: Un Municipio pertenece a un Departamento
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, verbose_name="Departamento")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        db_table = 'municipio' 

    def __str__(self):
        return f"{self.nombre} ({self.departamento.nombre})"

# --- 2. Modelos de Productos ---

class LineaProducto(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de Línea")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    
    class Meta:
        verbose_name = "Línea de Producto"
        verbose_name_plural = "Líneas de Producto"
        db_table = 'linea_producto'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código de Producto")
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Unitario")
    stock = models.IntegerField(default=0, verbose_name="Stock")
    aplica_iva = models.BooleanField(default=True, verbose_name="Aplica IVA")
    # Relación: Un Producto pertenece a una Línea
    linea_producto = models.ForeignKey(LineaProducto, on_delete=models.PROTECT, verbose_name="Línea de Producto")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = 'producto'

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

class ProductoImagen(models.Model):
    # Este modelo podría ser el que maneje el almacenamiento de las URLs o IDs 
    # de las imágenes en tu base de datos NoSQL externa (si usas GridFS o AWS S3, etc.)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    url_imagen = models.URLField(max_length=500, verbose_name="URL de la Imagen")
    es_principal = models.BooleanField(default=False, verbose_name="Imagen Principal")

    class Meta:
        verbose_name = "Imagen de Producto"
        verbose_name_plural = "Imágenes de Producto"
        db_table = 'producto_imagen'

    def __str__(self):
        return f"Imagen de {self.producto.nombre}"


# --- 3. Modelos de Clientes y Usuarios ---

class Cliente(models.Model):
    TIPO_PAGO_CHOICES = [
        ('CONTADO', 'Contado'),
        ('CREDITO', 'Crédito'),
        ('MIXTO', 'Mixto'),
    ]
    
    nombre = models.CharField(max_length=200)
    identificacion = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    tipo_pago = models.CharField(max_length=10, choices=TIPO_PAGO_CHOICES, default='CONTADO')
    municipio = models.CharField(max_length=100, verbose_name="Municipio de Residencia")

    # <--- ¡NUEVOS CAMPOS AÑADIDOS! --->
    tipo_documento = models.CharField(max_length=50, default='NIT', verbose_name="Tipo de Documento")
    estado = models.CharField(max_length=50, default='Activo', verbose_name="Estado del Cliente")
    # <-------------------------------->

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = 'cliente'

    def __str__(self):
        return self.nombre

# Django ya tiene un modelo 'User' para la autenticación, 
# pero si necesitas un perfil de usuario propio:
class Usuario(models.Model):
    # Si quieres usar el sistema de autenticación de Django, usa:
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=150)
    rol = models.CharField(max_length=50, verbose_name="Rol en el Sistema") # Ej: Vendedor, Administrador

    class Meta:
        verbose_name = "Usuario del Sistema"
        verbose_name_plural = "Usuarios del Sistema"
        db_table = 'usuario'

    def __str__(self):
        return self.nombre_completo


# --- 4. Modelos de Ventas (Transacciones) ---

class Venta(models.Model):
    FORMA_PAGO_CHOICES = [
        ('CONTADO', 'Contado'),
        ('CREDITO', 'Crédito'),
    ]

    numero_factura = models.CharField(max_length=50, unique=True, verbose_name="Número de Factura")
    fecha_venta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora")
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name="Cliente")
    usuario_vendedor = models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name="Vendedor")
    forma_pago = models.CharField(max_length=10, choices=FORMA_PAGO_CHOICES, default='CONTADO', verbose_name="Forma de Pago")
    total_general = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name="Total General")

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        db_table = 'venta'

    def __str__(self):
        return f"Factura N° {self.numero_factura}"


class VentaDetalle(models.Model):
    # Relación: Un detalle pertenece a una Venta
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles', verbose_name="Venta")
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, verbose_name="Producto")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Unitario de Venta")
    porcentaje_iva = models.DecimalField(max_digits=5, decimal_places=2, default=0.19, verbose_name="Porcentaje IVA") # Ejemplo 19%
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Total Detalle")

    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalles de Venta"
        db_table = 'venta_detalle'
        # Esto asegura que no haya duplicados de producto en la misma venta, si lo deseas
        unique_together = ('venta', 'producto') 

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en Factura {self.venta.numero_factura}"