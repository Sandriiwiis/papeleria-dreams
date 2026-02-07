from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView

# IMPORTANTE: Importamos el modelo que acabamos de crear
from .models import Producto 

def landing(request):
    # Ya no escribimos la lista a mano.
    # Esta línea mágica trae TODOS los productos que creaste en el admin:
    productos = Producto.objects.all()
    
    context = {'productos': productos}
    return render(request, 'landing.html', context)

# ... (El resto de tus vistas register, dashboard, etc. déjalas igual) ...
def register(request):
    # ... tu código sigue igual ...
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@permission_required("login.view_user", raise_exception=True)
def vista_protegida_permiso(request):
    return HttpResponse("Acceso permitido por permiso")

class DashboardMixinView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

class VistaPermisoMixinView(PermissionRequiredMixin, TemplateView):
    permission_required = "login.view_user"
    template_name = "permiso.html"

def agregar_carrito(request, producto_id):
    # 1. Obtenemos el "carrito" de la sesión (o creamos una lista vacía si no existe)
    carrito = request.session.get('carrito', [])
    
    # 2. Agregamos el ID del producto que el usuario eligió
    carrito.append(producto_id)
    
    # 3. Guardamos los cambios en la sesión
    request.session['carrito'] = carrito
    
    # 4. Volvemos a la tienda
    return redirect('landing')

def limpiar_carrito(request):
    # Borra la memoria del carrito
    request.session['carrito'] = []
    return redirect('landing')

def ver_carrito(request):
    # 1. Recuperamos la lista de IDs de la sesión
    carrito_ids = request.session.get('carrito', [])
    
    # 2. Buscamos los productos reales en la base de datos
    productos_en_carrito = []
    total = 0
    
    for producto_id in carrito_ids:
        # Buscamos cada producto por su ID
        producto = Producto.objects.filter(id=producto_id).first()
        if producto:
            productos_en_carrito.append(producto)
            total += producto.precio
            
    # 3. Enviamos todo al template
    return render(request, 'carrito.html', {
        'productos': productos_en_carrito, 
        'total': total
    })