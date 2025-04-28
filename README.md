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

## 📦 Instalación

1. Cloná el repositorio:
```bash
git clone https://github.com/tu-usuario/TuPrimeraPagina.git
cd TuPrimeraPagina
```

2. Creá y activá el entorno virtual:
```bash
python -m venv .venv
.venv\Scripts\activate  
```

3. Instalá las dependencias:
```bash
pip install -r requirements.txt
```

4. Realizá las migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. (Opcional) Creá un superusuario:
```bash
python manage.py createsuperuser
```

6. Iniciá el servidor:
```bash
python manage.py runserver
```

---

## Funcionalidades principales

### 🏠 Página pública

- `/` → Inicio con bienvenida.
- `/vehiculos/` → Catálogo de vehículos con filtro por tipo, modelo y año.
- `/quienes/` → Información institucional.
- `/login/` y `/registro/` → Login unificado y registro de clientes.

---

### 👩‍💼 Vendedor (solo creados por consola o admin)

- **Inicio de sesión** → `/login/`
- **Redirección automática al panel** → `/panel-vendedor/`
- **Desde su panel puede:**
  - Cargar vehículos: `/vehiculos/nuevo/`
  - Ver vehículos cargados (disponibles o vendidos)
  - Editar y eliminar sus propios vehículos

---

### 👤 Cliente (registro web permitido)

- **Registro** → `/registro/`
- **Inicio de sesión** → `/login/`
- **Redirección automática al panel** → `/panel-cliente/`
- **Desde su panel puede:**
  - Ver su historial de compras
  - Ir a `/vehiculos/` y comprar vehículos disponibles

---

### 🛠 Panel de administración (`/admin/`)

- Superusuario puede gestionar:
  - Vehículos, Ventas, Vendedores y Clientes
  - Acciones personalizadas: marcar vehículos como disponibles / no disponibles

---

## 🧾 Requisitos de la consigna 

✔️ **Un formulario para insertar datos por cada modelo creado**: debido a la logica de negocio planteada, cada clase se crea de una forma distinta
- Vendedor: creado por consola o admin.
- Cliente: formulario en `/registro/`.
- Vehiculo: formulario exclusivo en el panel de vendedor.
- Venta: se genera automáticamente al comprar un vehículo.

✔️ **Un formulario para buscar algo en la BD**:
- Búsqueda de vehículos por modelo, tipo y año en `/vehiculos/`.

✔️ **Uso de herencia de plantillas (HTML)**:
- `index.html` como plantilla base.
- Todas las secciones (`Inicio`, `Vehículos`, `PanelVendedor`, etc.) extienden esta base.
- Organización clara en subcarpetas: `templates/concesionaria/...`.

✔️ **Aplicación del patrón MVT (Model - View - Template)**:
- Models para Vendedor, Cliente, Vehiculo y Venta.
- Views específicas para cada función: registro, login, compra, carga.
- Templates bien estructurados y reutilizables con bloques `{% block %}`.


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

## 📂 Estructura de templates

- `index.html` → base principal con herencia
- `templates/concesionaria/`
  - `Inicio/inicio.html`
  - `Vehiculos/vehiculos.html`, `crear_vehiculo.html`
  - `Login/login.html`
  - `PanelVendedor/panelVendedor.html`
  - `PanelCliente/panelCliente.html`
  - `Registro/registro.html`
  - `QuienesSomos/quienes.html`
