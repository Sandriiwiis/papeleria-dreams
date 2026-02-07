from django.urls import path
from django.contrib.auth import views as login_views
from django.views.generic import RedirectView
# AQUÍ ESTABA EL ERROR: Faltaba importar ver_carrito 👇
from .views import (
    landing,
    register,
    dashboard,
    vista_protegida_permiso,
    DashboardMixinView,
    VistaPermisoMixinView,
    agregar_carrito,
    limpiar_carrito,
    ver_carrito    # <--- ¡AHORA SÍ ESTÁ INVITADO!
)

urlpatterns = [
    path("", landing, name="landing"),

    path("login/", login_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", login_views.LogoutView.as_view(next_page='landing'), name="logout"), 
    path("register/", register, name="register"),
    path("dashboard/", dashboard, name="dashboard"),
    path("permiso/", vista_protegida_permiso, name="vista_permiso"),
    path("dashboard-mixin/", DashboardMixinView.as_view(), name="dashboard_mixin"),
    path("permiso-mixin/", VistaPermisoMixinView.as_view(), name="permiso_mixin"),

    # Rutas del Carrito
    path('agregar/<int:producto_id>/', agregar_carrito, name='agregar_carrito'),
    path('limpiar/', limpiar_carrito, name='limpiar_carrito'),
    path('carrito/', ver_carrito, name='ver_carrito'),

    # Redirect final (Siempre al último)
    path("<path:anything>", RedirectView.as_view(url="/", permanent=False)),
]