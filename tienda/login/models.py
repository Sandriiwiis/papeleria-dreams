from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.IntegerField()
    # Guardaremos el emoji aquí como texto. Ejemplo: 🎀
    imagen = models.CharField(max_length=100, default="🎀") 
    # Aquí guardamos el código de color. Ejemplo: #ffcfdf
    color = models.CharField(max_length=20, default="#ffcfdf", verbose_name="Color Fondo")

    def __str__(self):
        return f"{self.nombre} (${self.precio})"
    
class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0) # Usamos Integer porque los precios en Chile no suelen usar decimales

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.IntegerField()
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} (Pedido #{self.pedido.id})"