# Concesionaria San Pedro 🚗

Este proyecto es una aplicación web construida con Django como parte del curso. La temática es una concesionaria de vehículos con funcionalidades diferenciadas para vendedores y clientes.

🧠 Lógica de negocio

La aplicación representa una concesionaria de vehículos con flujos diferenciados para clientes y vendedores.

- Los **vendedores** son usuarios creados desde consola o por el administrador. Acceden a un **panel exclusivo** tras iniciar sesión, desde donde pueden:
  - Registrar nuevos vehículos
  - Editar o eliminar los vehículos que hayan cargado
  - Visualizar sus **vehículos disponibles**
  - Consultar los **vehículos vendidos**, con detalle de cliente, fecha y precio de venta

- Los **clientes** pueden registrarse desde la web. Al iniciar sesión son redirigidos a su **panel de cliente**, donde pueden:
  - Ver su **historial de compras**
  - Navegar el catálogo general de vehículos
  - Comprar vehículos disponibles con un solo clic, lo que genera automáticamente una **venta**, marca el vehículo como **no disponible**, y actualiza los paneles de ambas partes (cliente y vendedor)

- El **superusuario** accede al panel de administración (`/admin`) con privilegios para gestionar todos los modelos del sistema. Puede:
  - Ver, agregar, modificar o eliminar vendedores, clientes, vehículos y ventas
  - Ejecutar **acciones personalizadas**, como marcar múltiples vehículos como disponibles o no disponibles desde el listado de administración.
    
---

## 📋 Resumen cumplimiento de la consigna:

- **Existencia de `requirements.txt`:** 
Incluido y actualizado con Django, Pillow y demás dependencias.

- **Adaptar templates y views para manejar imágenes:** 
Todos los formularios (`Registro`, `Editar perfil`, `Crear/Editar Vehículo`) usan `enctype="multipart/form-data"` y reciben `request.FILES`.

- **Uso de mínimo 2 CBV:** 
`PanelVendedorView` y `LoginViewEmail` son `Class-Based Views`.

- **Uso de mínimo un mixin en una CBV:** 
`VendorRequiredMixin` combinado con `LoginRequiredMixin` en `PanelVendedorView`.

- **Uso de mínimo un decorador en una función-based view:** 
`@login_required` y validaciones con `HttpResponseForbidden` en `panel_cliente`, `comprar_vehiculo`, etc.

- **Una vista de “inicio”:**
  `concesionaria.views.inicio` en `/` renderiza `Inicio/inicio.html`.

- **Acceso a una vista “Acerca de mí” / “About”:** 
`concesionaria.views.about` en `/about/` con plantilla `Acerca de mí`.

- **Modelo principal con mín. 3 CharField, 1 ImageField, 1 DateField:** 
El modelo `Vehiculo` tiene `marca`, `modelo`, `tipo` (CharFields), `foto` (ImageField) y `año` (IntegerField).

- **Listado de objetos con búsqueda y mensaje si no hay resultados:** 
`/vehiculos/` y panel de vendedor incluyen filtros por modelo, tipo y año y muestran mensaje si no hay resultados.

- **Desde el listado: detalle, creación, edición y borrado:** 
Enlaces a `crear_vehiculo`, `editar_vehiculo`, `eliminar_vehiculo` directamente desde las listas.

- **Registrar en admin todos los modelos:** 
`Vehiculo`, `Venta`, `Vendedor` y `Cliente` registrados en `admin.py`.

- **Tener una app para autenticación:** 
App `cuentas` separada con login, logout, registro, perfil y edición de perfil.

- **Login / Logout / Registro de usuario:** 
Vistas basadas en `LoginView`, `LogoutView` (con plantilla) y función `registro_cliente`.

- **Registro pide username, email, password + avatar + fecha_nacimiento:** 
`ClienteRegistroForm` solicita email, password, nombre, apellido, DNI, teléfono, avatar y fecha de nacimiento.

- **Vista de perfil muestra nombre, apellido, email, avatar y fecha_nacimiento:** `
perfil.html` despliega todos estos campos.

- **Desde perfil: acceso a edición de datos + cambio de password:** 
`editar_perfil.html` incluye formularios para datos, email/avatar y sección opcional de cambio de contraseña con toggle JS.

- **Un formulario para insertar datos por cada modelo creado**: 
debido a la logica de negocio planteada, cada clase se crea de una forma distinta
  - Vendedor: creado por consola o admin.
  - Cliente: formulario en `/registro/`.
  - Vehiculo: formulario exclusivo en el panel de vendedor.
  - Venta: se genera automáticamente al comprar un vehículo.

- **Un formulario para buscar algo en la BD**:
Búsqueda de vehículos por modelo, tipo y año en `/vehiculos/`.

- **Uso de herencia de plantillas (HTML)**:
  - `base.html` como plantilla base.
  - Todas las secciones (`Inicio`, `Vehículos`, `PanelVendedor`, etc.) extienden esta base.
  - Organización clara en subcarpetas: `templates/concesionaria/...`.

- **Aplicación del patrón MVT (Model - View - Template)**:
  - Models para Vendedor, Cliente, Vehiculo y Venta.
  - Views específicas para cada función: registro, login, compra, carga.
  - Templates bien estructurados y reutilizables con bloques `{% block %}`.

---

## 👥 Roles y funcionalidades extra

### Vendedores

- **Panel de Vendedor** (`/panel-vendedor/`) implementado como CBV con mixins.  
- **Filtros** en tiempo real por marca, modelo y tipo.  
- **Listado** simplificado: _Modelo Marca – Tipo_.  
- **Botones**:
  - `✏️ Editar`
  - `🗑️ Eliminar`
  - `🔎 Ver más` despliega año, precio, disponibilidad y foto en un collapse.  
- **Carga rápida**: `+ Agregar Vehículo` al lado de “🔍 Filtrar”.  
- **Ventas realizadas**: tabla con vehículo, cliente, precio y fecha.  

### Clientes

- **Registro web** con avatar y fecha de nacimiento.  
- **Panel de Cliente** (`/panel-cliente/`):
  - Historial de compras con detalle de cada venta.  
  - Enlace al catálogo `/vehiculos/` para filtrar y comprar.  
- **Compra con un clic**: al comprar, se genera la venta, se marca el vehículo como no disponible y se actualizan ambos paneles.

---

### 🛠 Panel de administración (`/admin/`)

- Superusuario puede gestionar:
  - Vehículos, Ventas, Vendedores y Clientes
  - Acciones personalizadas: marcar vehículos como disponibles / no disponibles

---

## 🛠 Tecnologías y librerías

- **Python 3.12**, **Django 5.2**  
- **Bootstrap 5** para estilos y componentes JS (collapse, grid).  
- **Pillow** para el manejo de ImageFields (avatares, fotos de vehículos).  
- **SQLite** como base de datos por defecto.  

---

## 🚀 Instalación y puesta en marcha

1. Clonar el repositorio y situarse en la carpeta del proyecto.  
2. Crear y activar el virtualenv:

    ```bash
    python -m venv .venv
    # Windows PowerShell
    .\.venv\Scripts\Activate.ps1
    # o Git Bash / WSL
    source .venv/Scripts/activate
    ```

3. Instalar dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Migrar modelos:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. (Opcional) Crear superusuario:

    ```bash
    python manage.py createsuperuser
    ```

6. Levantar el servidor:

    ```bash
    python manage.py runserver
    ```

---

## ✅ Orden sugerido para probar

1. Crear un superusuario e ingresar a `/admin/`.
2. Crear un **vendedor** desde consola o admin:
```python
from concesionaria.models import Vendedor
v = Vendedor.objects.create_user(email="vendedor@demo.com", password="clave1234", username="vendedor")
```
3. Iniciar sesión como vendedor y cargar vehículos.
4. Registrar un cliente desde `/registro/`.
5. Iniciar sesión como cliente y comprar un vehículo.
6. Verificar que:
   - El vehículo desaparece de la lista.
   - Aparece en el historial del cliente.
   - Aparece como vendido en el panel del vendedor.

---

## 📂 Estructura de carpetas clave

```
.
├── concesionaria/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/concesionaria/
├── cuentas/
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/cuentas/
├── media/
├── static/
├── requirements.txt
└── README.md
```

## 📂 Estructura de templates

- `base.html`
- `templates/concesionaria/`
  - `Inicio/inicio.html`
  - `Vehiculos/vehiculos.html`, `crear_vehiculo.html`, `editar_vehiculo.html`, `confirmar_eliminar.html`
  - `QuienesSomos/quienes.html`
  - `Acerca de mí/About.html`
- `templates/cuentas/`
  - `Login/login.html`
  - `Registro/registro.html`
  - `Perfil/perfil.html`
  - `Perfil/editar_perfil.html`
  - `Logout/logout.html`
