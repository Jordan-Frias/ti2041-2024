Gestión de Productos S.A.

Este proyecto es una aplicación web desarrollada en Django que permite la gestión de productos de una empresa. Los usuarios pueden registrar, consultar, actualizar y eliminar productos a través de una interfaz web amigable.

Instrucciones de Utilización de la Página

Paso 1: Clonar o descargar los archivos del repositorio:

git clone <URL_DEL_REPOSITORIO>

Paso 2: Instalar Visual Studio Code para ejecutar el proyecto e instalar Python.

Paso 3: Instalar Django y las dependencias:

pip install --upgrade pip
pip install django

Paso 4: Ejecutar el servidor de desarrollo:

python manage.py runserver

Paso 5: Una vez dado el link, hacer clic en él. En este entorno podrás rellenar el formulario con los productos y también visualizarlos.

Usuarios

Usuario: admin               Usuario: ADMIN_PRODUCTS

Contraseña: inacap2024       Contraseña: inacap2024

Medidas de Seguridad Implementadas

Autenticación de Usuario

Se ha implementado un servicio de login en la raíz de la aplicación (/) para autenticar a los usuarios antes de permitir el acceso al catálogo de productos. Esto se logra usando LoginView de Django.

path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

Restricción de Acceso a Vistas Específicas

Se han restringido las vistas que muestran los productos y la administración de los productos para que solo los usuarios autenticados puedan acceder. Esto se realizó mediante el uso del decorador @login_required.

@login_required
def consulta_productos(request):
    # Lógica para mostrar productos

Autorización basada en Grupos

Se ha utilizado un grupo específico llamado ADMIN_PRODUCTS para permitir que ciertos usuarios puedan realizar acciones de CRUD sobre los productos. Solo los usuarios pertenecientes a este grupo pueden acceder a estas funcionalidades. Además, el grupo ADMIN_PRODUCTS no tiene acceso a la sesión de administración general de Django, garantizando así una segmentación de permisos adecuada.

@user_passes_test(is_admin_products)
def administrar_productos(request):
    # Lógica para la administración de productos

Estas medidas se implementaron para asegurar la autenticación y autorización dentro de la aplicación, limitando el acceso solo a los usuarios autorizados para mejorar la seguridad del sistema.

Características

Registro de nuevos productos.

Consulta del catálogo de productos.

Actualización y eliminación de productos (solo para usuarios con permisos).

Tecnologías Utilizadas

Python

Django

HTML/CSS

Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

gestion_productos/ - Contiene los archivos de configuración del proyecto Django.

productos/ - Contiene la lógica de la aplicación, incluyendo modelos, vistas y formularios.

templates/ - Contiene los archivos HTML para las vistas de la aplicación.

static/ - Contiene los archivos CSS y otros elementos estáticos.
