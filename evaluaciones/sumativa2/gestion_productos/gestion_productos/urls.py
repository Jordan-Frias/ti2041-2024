from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from productos import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Ahora admin estará correctamente definido
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Página de inicio como login
    path('registro/', views.registro_producto, name='registro_producto'),
    path('consulta/', views.consulta_productos, name='consulta_productos'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
