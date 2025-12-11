Versión en inglés disponible en [README.md](README.md).

# Concesionaria San Pedro — Aplicación web Django 🚗

Aplicación web monolítica construida con Django para una concesionaria de vehículos. Gestiona flujos diferenciados para vendedores y clientes y ofrece un panel de administración para superusuarios. La UI se renderiza con templates de Django y estilos Bootstrap; no existe una SPA separada ni una API REST expuesta.

## 1. Contexto académico y consigna 🎓
Proyecto desarrollado como trabajo práctico de un curso de Django. La consigna exige:
- Sitio funcional para una concesionaria con roles diferenciados.
- Manejo de imágenes (vehículos y avatares) en formularios con `multipart/form-data`.
- Al menos 2 Class-Based Views (CBV) y 1 mixin en CBV.
- Uso de un decorador en una Function-Based View.
- Vista de inicio y vista “Acerca de”.
- Aplicación del patrón MVT y herencia de plantillas.

## 2. Lógica de negocio y roles 🧩
### Vendedores (modelo `Vendedor`)
- Acceden a un panel exclusivo tras iniciar sesión.
- Registrar, editar o eliminar vehículos propios.
- Ver vehículos disponibles y ventas realizadas con cliente, fecha y precio.
- Filtrar vehículos por marca, modelo y tipo.

### Clientes (perfil `Cliente`)
- Registro web con avatar y fecha de nacimiento.
- Panel de cliente con historial de compras.
- Navegar el catálogo general y comprar vehículos disponibles con un clic; la compra crea una `Venta`, marca el vehículo como no disponible y actualiza ambos paneles.

### Superusuario (admin)
- Gestiona todos los modelos desde `/admin`.
- Puede marcar múltiples vehículos como disponibles/no disponibles con acciones masivas.

### Flujos adicionales
- Catálogo público `/vehiculos/` con filtros por modelo, tipo y año, y mensaje de vacío.
- Compra rápida sin pasos intermedios; impacta en panel de cliente y vendedor.

## 3. Resumen de cumplimiento de la consigna
- `requirements.txt` incluido (Django, Pillow y dependencias mínimas).
- Formularios manejan imágenes con `enctype="multipart/form-data"` y `request.FILES`.
- Mínimo 2 CBV: `PanelVendedorView` y `LoginViewEmail`.
- Mínimo 1 mixin en CBV: `VendorRequiredMixin` + `LoginRequiredMixin` en `PanelVendedorView`.
- Decoradores en FBV: `@login_required` y validaciones con `HttpResponseForbidden` en vistas como `comprar_vehiculo`.
- Vista de inicio: `concesionaria.views.inicio` → `Inicio/inicio.html`.
- Vista Acerca de: `concesionaria.views.about` → `Acerca de mi/About.html`.
- Modelo principal con 3 `CharField`, 1 `ImageField`, 1 campo de fecha/entero: `Vehiculo` con `marca`, `modelo`, `tipo`, `foto`, `año`.
- Listado con búsqueda y mensaje vacío: `/vehiculos/` y panel de vendedor.
- Desde listados: enlaces a crear, editar y eliminar vehículos.
- Modelos registrados en admin: `Vehiculo`, `Venta`, `Vendedor`, `Cliente`.
- App de autenticación separada (`cuentas`) con login, logout, registro, perfil y edición de perfil.
- Login/Logout/Registro implementados con `LoginView`, `LogoutView` y `registro_cliente`.
- Registro solicita username/email/password + avatar + fecha de nacimiento.
- Perfil muestra nombre, apellido, email, avatar y fecha de nacimiento; desde perfil se accede a edición y cambio de password.
- Un formulario por modelo: Vendedor (consola/admin), Cliente (web `/registro/`), Vehículo (panel vendedor), Venta (automática al comprar).
- Formulario de búsqueda en BD: filtros de vehículos por modelo, tipo y año.
- Herencia de plantillas con `base.html`.
- Patrón MVT aplicado con modelos, views y templates específicos.

## 4. Funcionalidades extra
### Vendedores
- Panel de vendedor (`/panel-vendedor/`) como CBV con mixins.
- Filtros en tiempo real por marca, modelo y tipo.
- Listado simplificado; botones de editar/eliminar y detalle expandible (año, precio, disponibilidad, foto).
- Acceso rápido “+ Agregar Vehículo” junto a filtros.
- Tabla de ventas realizadas con vehículo, cliente, precio y fecha.

### Clientes
- Registro web con avatar y fecha de nacimiento.
- Panel `/panel-cliente/` con historial de compras y acceso al catálogo para comprar.
- Compra en un clic: genera `Venta`, marca no disponible y actualiza paneles.

### Admin `/admin/`
- Gestión completa de Vehículos, Ventas, Vendedores y Clientes.
- Acciones personalizadas para disponibilidad de vehículos.

## 5. Resumen técnico 🛠️
- **Tipo de app:** Monolito Django con templates; sin SPA ni API REST.
- **Backend:** Python 3.12, Django 5.2, ORM de Django, usuario custom `Vendedor` (email como `USERNAME_FIELD`), perfil `Cliente`.
- **Frontend:** Templates de Django + Bootstrap 5 (CDN).
- **Base de datos:** SQLite por defecto.
- **Medios:** `ImageField` para vehículos y avatares; Pillow para manejo de imágenes.
- **Dependencias clave:** Django, Pillow, sqlparse, tzdata (ver `requirements.txt`).

## 6. Arquitectura y estructura 🧱
- `TuPrimeraPagina/`: configuración del proyecto (settings, urls, wsgi/asgi).
- `concesionaria/`: lógica de negocio (`Vehiculo`, `Venta`; catálogo, compra, CRUD de vehículos; admin; templates específicos).
- `cuentas/`: autenticación y perfiles (`Vendedor` custom, `Cliente`; paneles como CBV; formularios y mixins de acceso).
- `templates/`: plantilla base `base.html` extendida por todas las vistas.
- `media/`: ejemplos de avatares y fotos de vehículos versionados para demo.
- `requirements.txt`: dependencias mínimas para desarrollo.

**Estructura de carpetas clave**
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
├── templates/
│   └── base.html
├── requirements.txt
├── manage.py
└── README.md / README_ES.md
```

**Estructura de templates**
- `base.html`
- `templates/concesionaria/`
  - `Inicio/inicio.html`
  - `Vehiculos/vehiculos.html`, `crear_vehiculo.html`, `editar_vehiculo.html`, `confirmar_eliminar.html`
  - `QuienesSomos/quienes.html`
  - `Acerca de mi/About.html`
- `templates/cuentas/`
  - `Login/login.html`
  - `Registro/registro.html`
  - `Perfil/perfil.html`
  - `Perfil/editar_perfil.html`
  - `Logout/logout.html`

## 7. Instalación y configuración ⚙️
1) Clonar el repositorio y ubicarse en la carpeta del proyecto.  
2) Crear y activar un entorno virtual:
```bash
python -m venv .venv
# PowerShell
.\.venv\Scripts\Activate.ps1
# Git Bash / WSL
source .venv/Scripts/activate
```
3) Instalar dependencias:
```bash
pip install -r requirements.txt
```
4) Aplicar migraciones de la base de datos:
```bash
python manage.py makemigrations
python manage.py migrate
```
5) (Opcional) Crear superusuario:
```bash
python manage.py createsuperuser
```

## 8. Cómo ejecutar la aplicación
```bash
python manage.py runserver
```
Abrir `http://127.0.0.1:8000/` en el navegador.

## 9. Usuarios de demo (ya creados) 👥
- Vendedores:
  - `vendedor1@demo.com` / `Clave123!`
  - `vendedor2@demo.com` / `Clave123!`
  - `vendedor3@demo.com` / `Clave123!`
- Vehículos de ejemplo: 9 cargados (3 autos, 3 camionetas, 3 motos) asociados a esos vendedores y marcados como disponibles.

## 9.1 Orden sugerido para probar 🧪
1. Crear un superusuario e ingresar a `/admin/`.  
2. Crear un vendedor desde consola o admin:
   ```python
   from concesionaria.models import Vendedor
   v = Vendedor.objects.create_user(
       email="vendedor@demo.com",
       password="clave1234",
       username="vendedor"
   )
   ```
3. Iniciar sesión como vendedor y cargar vehículos.  
4. Registrar un cliente desde `/registro/`.  
5. Iniciar sesión como cliente y comprar un vehículo.  
6. Verificar:
   - El vehículo desaparece del listado disponible.
   - Aparece en el historial del cliente.
   - Aparece como vendido en el panel del vendedor.

## 10. Configuración por entorno 🌐
- Variables esperadas para despliegue:
  - `DJANGO_SECRET_KEY`: clave secreta (no versionar).
  - `DJANGO_DEBUG`: `False` en producción.
  - `DJANGO_ALLOWED_HOSTS`: lista separada por comas de hosts permitidos.

## 11. Mejoras futuras
- Añadir pruebas unitarias e integración para flujos clave (registro, compra, permisos de paneles).
- Endurecer configuración de seguridad en producción (DEBUG=False, hosts, CSRF/HTTPS).
- Asegurar que acciones sensibles (p. ej., compra) requieran métodos POST con CSRF.
- Normalizar nombres de campos a ASCII (`año` → `anio`) para portabilidad.
- Agregar Docker/Compose para setup y un pipeline de CI para pruebas y linting.
