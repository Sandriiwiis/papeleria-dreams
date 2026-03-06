from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
import urllib.parse # Importación movida arriba para mantener el orden

# Importamos los modelos de productos y los nuevos modelos de pedidos
from .models import Producto, Pedido, DetallePedido

def landing(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'landing.html', context)

def register(request):
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
    carrito = request.session.get('carrito', [])
    carrito.append(producto_id)
    request.session['carrito'] = carrito
    return redirect('landing')

def limpiar_carrito(request):
    request.session['carrito'] = []
    return redirect('landing')

def ver_carrito(request):
    carrito_ids = request.session.get('carrito', [])
    productos_en_carrito = []
    total = 0
    
    for producto_id in carrito_ids:
        producto = Producto.objects.filter(id=producto_id).first()
        if producto:
            productos_en_carrito.append(producto)
            total += producto.precio
            
    return render(request, 'carrito.html', {
        'productos': productos_en_carrito, 
        'total': total
    })

# Decorador agregado: ¡Solo los usuarios logueados pueden comprar!
@login_required(login_url='login')
def procesar_pago_whatsapp(request):
    carrito_ids = request.session.get('carrito', [])
    
    # Si por algún motivo el carrito está vacío, devolvemos al usuario a la tienda
    if not carrito_ids:
        return redirect('landing')
        
    # 1. Crear el Pedido general en la base de datos vinculado al usuario actual
    nuevo_pedido = Pedido.objects.create(usuario=request.user, total=0)
    
    telefono = "56912345678" 
    mensaje = "¡Hola Papelería Dreams! 💖 Me encantaría concretar el pago de este pedido:\n\n"
    total_calculado = 0
    
    # 2. Buscar productos, guardar el detalle en la BD y armar el mensaje
    for producto_id in carrito_ids:
        producto = Producto.objects.filter(id=producto_id).first()
        if producto:
            # Creamos el detalle específico para este pedido
            DetallePedido.objects.create(
                pedido=nuevo_pedido,
                producto=producto,
                precio=producto.precio,
                cantidad=1
            )
            mensaje += f"✨ {producto.nombre} - ${producto.precio}\n"
            total_calculado += producto.precio
            
    # 3. Actualizamos el precio final en el registro del pedido
    nuevo_pedido.total = total_calculado
    nuevo_pedido.save()
    
    # 4. Finalizamos el mensaje para WhatsApp
    mensaje += f"\nTotal a pagar: ${total_calculado}\n¡Muchas gracias!"
    mensaje_codificado = urllib.parse.quote(mensaje)
    whatsapp_url = f"https://wa.me/{telefono}?text={mensaje_codificado}"
    
    # 5. Vaciamos el carrito de la sesión
    request.session['carrito'] = []
    
    # 6. Redirigimos a WhatsApp
    return redirect(whatsapp_url)