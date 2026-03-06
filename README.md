# 🌸 Papelería Dreams - Proyecto Django E-commerce

**Autor:** Sandra
**Curso:** Fullstack Python - Módulo 8 (Entrega Final de Portafolio)
**Fecha:** Marzo 2026
**Enlace al Repositorio:** [https://github.com/Sandriiwiis/papeleria-dreams](https://github.com/Sandriiwiis/papeleria-dreams)

---

## 📝 Descripción del Proyecto
Este proyecto consiste en el desarrollo de una aplicación web (E-commerce MVP) para una tienda de papelería ("Papelería Dreams"). La aplicación implementa el patrón de arquitectura **MVT (Modelo-Vista-Plantilla)** de Django, integrando todo lo aprendido a lo largo del bootcamp. 

El flujo principal permite a los usuarios navegar por un catálogo dinámico, gestionar un carrito de compras y registrar sus pedidos en la base de datos, culminando en una redirección directa a WhatsApp para una atención personalizada.

---

## ✨ Funcionalidades Implementadas

1.  **Autenticación y Roles:**
    * Sistema de Registro, Login y Logout.
    * Roles definidos: **Cliente** (acceso a compras) y **Administrador** (gestión de catálogo).
    * Protección de rutas mediante decoradores (`@login_required`).

2.  **Catálogo y Persistencia (Base de Datos):**
    * Modelos en SQLite3 gestionados a través del ORM de Django.
    * Panel de Administración (`/admin`) para operaciones CRUD sobre los productos.

3.  **Carrito y Flujo de Compra (Lógica de Negocio):**
    * Uso de **Sesiones** temporales (`request.session`) para agregar, ver y vaciar productos del carrito.
    * **Confirmación de compra:** Al proceder al pago, el sistema genera automáticamente un `Pedido` y su `DetallePedido` en la base de datos, asociándolos al usuario autenticado.
    * Integración dinámica con la API de **WhatsApp** (`wa.me`) para concretar el pago y mejorar la experiencia del cliente.

4.  **Interfaz de Usuario (UX/UI):**
    * Diseño responsivo utilizando **Bootstrap 5**.
    * Estilización personalizada (CSS) con temática "Pastel/Cute".
    * Mensajes de éxito/error y validaciones para guiar al usuario.

---

## 🗺️ Rutas Principales

* `/` : Catálogo de productos (Landing Page).
* `/login/` y `/register/` : Accesos de usuario.
* `/carrito/` : Resumen de la compra y total a pagar.
* `/pagar-whatsapp/` : Procesamiento del pedido en BD y redirección a WhatsApp.
* `/admin/` : Panel de administración exclusivo para el staff.

---

## 🔑 Credenciales de Prueba

Para evaluar el funcionamiento integral de la plataforma, se han creado las siguientes cuentas de prueba:

* **Administrador (Staff):**
  * Usuario: `Sandra` 
  * Contraseña: `Admin1234`
* **Cliente (Usuario regular):**
  * Usuario: `Cereza` 
  * Contraseña: `Cere1234` 

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.14
* **Framework:** Django 6.0
* **Base de Datos:** SQLite3
* **Frontend:** HTML5, CSS3, Bootstrap 5.3
* **Control de Versiones:** Git / GitHub

---

## ⚙️ Instrucciones de Instalación y Ejecución

Si desea correr este proyecto localmente:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/Sandriiwiis/papeleria-dreams](https://github.com/Sandriiwiis/papeleria-dreams)
    ```

2.  **Activar entorno virtual:**
    ```bash
    source venv/bin/activate  # En Mac/Linux
    venv\Scripts\activate     # En Windows
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install django
    ```

4.  **Ejecutar migraciones (para inicializar los modelos de Productos y Pedidos):**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Iniciar servidor local:**
    ```bash
    python manage.py runserver
    ```