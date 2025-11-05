from djongo import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=50, default='vendedor')

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos_vendidos = models.JSONField()  # [{producto_id, cantidad}]
    total = models.FloatField()

    def __str__(self):
        return f"Venta {self.id} - {self.cliente.nombre}"
