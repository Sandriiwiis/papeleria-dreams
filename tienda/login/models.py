from django.db import models

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