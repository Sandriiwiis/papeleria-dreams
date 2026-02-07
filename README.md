# 🌸 Papelería Dreams - Proyecto Django

**Autor:** Sandra
**Curso:** Fullstack Python - Módulo 6
**Fecha:** Febrero 2026

---

## 📝 Descripción del Proyecto
Este proyecto consiste en el desarrollo de una aplicación web para una tienda de papelería ("Papelería Dreams"). La aplicación implementa el patrón de arquitectura **MVT (Modelo-Vista-Plantilla)** de Django, permitiendo a los usuarios navegar por un catálogo de productos, registrarse, iniciar sesión y gestionar un carrito de compras dinámico.

El objetivo principal fue integrar la autenticación de usuarios con el manejo de datos persistentes (Base de Datos SQLite) y temporales (Sesiones de Django).

---

## ✨ Funcionalidades Implementadas

1.  **Autenticación de Usuarios:**
    * Sistema de Registro (`UserCreationForm`).
    * Inicio de Sesión (Login) y Cierre de Sesión (Logout).
    * Protección de rutas: El Dashboard y el Carrito son exclusivos para usuarios logueados.

2.  **Gestión de Productos (Administrador):**
    * Modelo `Producto` creado en base de datos.
    * Panel de Administración (`/admin`) habilitado para crear, editar y eliminar productos.
    * Carga dinámica de productos en la página de inicio (Landing Page).

3.  **Carrito de Compras (Lógica de Negocio):**
    * Implementación de **Sessions** para mantener el estado del carrito.
    * Funciones para `agregar`, `ver` y `vaciar` el carrito.
    * Cálculo automático del total a pagar.

4.  **Interfaz de Usuario (Frontend):**
    * Diseño responsivo utilizando **Bootstrap 5**.
    * Estilización personalizada (CSS) con temática "Pastel/Cute".
    * Uso de herencia de plantillas (`base.html`) para mantener la consistencia visual.

---

## 🧠 Reflexión del Desarrollador

Durante el desarrollo de este proyecto, profundicé en la comprensión de cómo Django maneja las peticiones HTTP y la importancia del archivo `urls.py` para el enrutamiento correcto.

Uno de los mayores desafíos fue la implementación del **Carrito de Compras**. Aprendí que, a diferencia de los productos que residen en la base de datos, el carrito es una estructura temporal que debe gestionarse mediante **Sesiones (`request.session`)**. Esto me permitió entender la diferencia entre datos persistentes y datos de sesión.

También me enfrenté a errores comunes como `TemplateDoesNotExist` o problemas de importación en las vistas, lo cual reforzó mi habilidad para depurar código leyendo los mensajes de error de la consola. Finalmente, logré integrar el Frontend (Bootstrap) con el Backend, asegurando que los botones (que inicialmente eran estáticos) ejecutaran acciones reales en el servidor.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.14
* **Framework:** Django 6.0
* **Base de Datos:** SQLite3
* **Frontend:** HTML5, CSS3, Bootstrap 5.3
* **Control de Versiones:** Git

---

## ⚙️ Instrucciones de Ejecución

Si desea correr este proyecto localmente:

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/Sandriiwiis/papeleria-dreams
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

4.  **Ejecutar migraciones:**
    ```bash
    python manage.py migrate
    ```

5.  **Crear superusuario (opcional):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Iniciar servidor:**
    ```bash
    python manage.py runserver
    ```