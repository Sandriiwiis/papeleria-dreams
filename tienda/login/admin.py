
# Register your models here.
from django.contrib import admin
from .models import Producto

# Esto hace que el diseño en el admin se vea ordenado
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'imagen')

admin.site.register(Producto, ProductoAdmin)