from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    primer_nombre = models.CharField(max_length=30, blank=True, null=True)
    segundo_nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=30, blank=True, null=True)
    apellido_materno = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.PositiveIntegerField()  # Cambiado a PositiveIntegerField
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre
    

class BoletaCompra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    estado_pedido = models.CharField(max_length=20, default='recibido')

    def __str__(self):
        return f"Boleta #{self.id} - {self.usuario.username}"

class DetalleCompra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    boletacompra = models.ForeignKey(BoletaCompra, on_delete=models.CASCADE, related_name='detalles')

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} - {self.subtotal} $"