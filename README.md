Spanish version available in [README_ES.md](README_ES.md).

# Django-car-dealership — Django Web App

Django monolith for a car dealership with distinct flows for sellers and customers, plus an admin panel for superusers. The UI is server-rendered with Django templates and Bootstrap; there is no separate SPA or exposed REST API.

## 1. Academic context / assignment 🎓
Built as a course assignment. The brief requires:
- Functional dealership site with differentiated roles.
- Image handling (vehicles and avatars) using `multipart/form-data`.
- At least 2 Class-Based Views (CBV) and 1 mixin in a CBV.
- A decorator on a Function-Based View.
- Home view and About view.
- MVT pattern with template inheritance.

## 2. Business logic and roles 🧩
### Sellers (`Vendedor` model)
- Access a dedicated dashboard after login.
- Create, edit, and delete their own vehicles.
- View available vehicles and their completed sales (customer, date, price).
- Filter vehicles by brand, model, and type.

### Customers (`Cliente` profile)
- Self-register with avatar and birthdate.
- Customer dashboard with purchase history.
- Browse the catalog and buy available vehicles in one click; the purchase creates a `Venta`, marks the vehicle unavailable, and updates both dashboards.

### Superuser (admin)
- Manages all models from `/admin`.
- Bulk actions to mark vehicles as available/unavailable.

### Additional flows
- Public catalog `/vehiculos/` with filters by model, type, and year, plus empty-state messaging.
- One-click purchase flows reflected in both seller and customer panels.

## 3. Assignment compliance checklist
- `requirements.txt` included (Django, Pillow, minimal deps).
- Forms handle images with `enctype="multipart/form-data"` and `request.FILES`.
- At least 2 CBVs: `PanelVendedorView` and `LoginViewEmail`.
- At least 1 mixin in CBV: `VendorRequiredMixin` + `LoginRequiredMixin` on `PanelVendedorView`.
- Decorators on FBVs: `@login_required` and `HttpResponseForbidden` checks (e.g., `comprar_vehiculo`).
- Home view: `concesionaria.views.inicio` → `Inicio/inicio.html`.
- About view: `concesionaria.views.about` → `Acerca de mi/About.html`.
- Main model with 3 `CharField`, 1 `ImageField`, 1 date/integer field: `Vehiculo` with `marca`, `modelo`, `tipo`, `foto`, `año`.
- Listings with search and empty message: `/vehiculos/` and seller dashboard.
- From listings you can create, edit, and delete vehicles.
- All models registered in admin: `Vehiculo`, `Venta`, `Vendedor`, `Cliente`.
- Separate auth app (`cuentas`) with login, logout, registration, profile, and profile edit.
- Login/Logout/Registration via `LoginView`, `LogoutView`, and `registro_cliente`.
- Registration collects username/email/password + avatar + birthdate.
- Profile shows name, surname, email, avatar, and birthdate; profile page links to edit and password change.
- One form to insert data per model: Seller (console/admin), Customer (`/registro/`), Vehicle (seller panel), Sale (automatic on purchase).
- Search form in DB: vehicle filters by model, type, and year.
- Template inheritance via `base.html`.
- MVT pattern with dedicated models, views, and templates.

## 4. Extra features
### Sellers
- Seller dashboard (`/panel-vendedor/`) as a CBV with mixins.
- Real-time filters by brand, model, and type.
- Simplified listing with edit/delete and expandable detail (year, price, availability, photo).
- Quick “+ Add Vehicle” shortcut next to filters.
- Sales table with vehicle, customer, price, and date.

### Customers
- Web registration with avatar and birthdate.
- `/panel-cliente/` with purchase history and link to catalog to buy.
- One-click purchase updates availability and dashboards.

### Admin `/admin/`
- Full CRUD for Vehicles, Sales, Sellers, and Customers.
- Custom actions to toggle vehicle availability.

## 5. Technical overview 🛠️
- **App type:** Django monolith with templates; no SPA or REST API layer.
- **Backend:** Python 3.12, Django 5.2, Django ORM, custom user `Vendedor` (email as `USERNAME_FIELD`), `Cliente` profile.
- **Frontend:** Django templates + Bootstrap 5 (CDN).
- **Database:** SQLite by default.
- **Media:** `ImageField` for vehicles and avatars; Pillow for image handling.
- **Dependencies:** Django, Pillow, sqlparse, tzdata (see `requirements.txt`).

## 6. Architecture and structure 🧱
- `TuPrimeraPagina/`: project config (settings, urls, wsgi/asgi).
- `concesionaria/`: business logic (`Vehiculo`, `Venta`; catalog, purchase, vehicle CRUD; admin; templates).
- `cuentas/`: auth and profiles (custom `Vendedor`, `Cliente`; dashboards as CBVs; forms and access mixins).
- `templates/`: base layout `base.html` extended by all pages.
- `media/`: sample avatars and vehicle photos checked in for demo.
- `requirements.txt`: minimal development dependencies.

**Key folder structure**
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

**Template structure**
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

## 7. Installation & setup ⚙️
1) Clone the repo and move into the project directory.  
2) Create and activate a virtualenv:
```bash
python -m venv .venv
# PowerShell
.\.venv\Scripts\Activate.ps1
# Git Bash / WSL
source .venv/Scripts/activate
```
3) Install dependencies:
```bash
pip install -r requirements.txt
```
4) Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
5) (Optional) Create a superuser:
```bash
python manage.py createsuperuser
```

## 8. How to run
```bash
python manage.py runserver
```
Open `http://127.0.0.1:8000/` in your browser.

## 9. Demo users (preloaded) 👥
- Sellers:
  - `vendedor1@demo.com` / `Clave123!`
  - `vendedor2@demo.com` / `Clave123!`
  - `vendedor3@demo.com` / `Clave123!`
- Sample vehicles: 9 items (3 cars, 3 trucks, 3 bikes) assigned to those sellers and marked as available.

## 9.1 Suggested test flow 🧪
1. Create a superuser and log in to `/admin/`.  
2. Create a seller via console/admin:
   ```python
   from concesionaria.models import Vendedor
   v = Vendedor.objects.create_user(
       email="vendedor@demo.com",
       password="clave1234",
       username="vendedor"
   )
   ```
3. Log in as the seller and add vehicles.  
4. Register a customer at `/registro/`.  
5. Log in as the customer and purchase a vehicle.  
6. Verify:
   - The vehicle disappears from the available list.
   - It appears in the customer's history.
   - It appears as sold in the seller's panel.

## 10. Environment configuration 🌐
- Expected variables for deployment:
  - `DJANGO_SECRET_KEY`: secret key (do not commit).
  - `DJANGO_DEBUG`: set to `False` in production.
  - `DJANGO_ALLOWED_HOSTS`: comma-separated list of allowed hosts.

## 11. Future work
- Add unit/integration tests for key flows (registration, purchase, dashboard permissions).
- Harden production security (DEBUG=False, allowed hosts, CSRF/HTTPS).
- Ensure sensitive actions (e.g., purchase) are POST-only with CSRF protection.
- Normalize field names to ASCII (`año` → `anio`) for portability.
- Provide Docker/Compose for setup and a CI pipeline for tests and linting.
