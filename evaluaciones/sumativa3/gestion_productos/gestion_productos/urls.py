from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from productos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # La raíz muestra el login
    path('logout/', views.logout_view, name='logout'),  # Usamos la vista personalizada para logout
    path('productos/', views.consulta_productos, name='consulta_productos'),  # Catálogo de productos con el nombre 'consulta_productos'
    path('registro/', views.registro_producto, name='registro_producto'),  # Ruta para registrar productos
    path('base/', views.base_view, name='base'),  # Página principal después del login
    path('agregar/', views.agregar_producto, name='agregar_producto'),  # Ruta para agregar un producto
    path('actualizar/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),  # Actualizar producto
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),  # Eliminar producto
]