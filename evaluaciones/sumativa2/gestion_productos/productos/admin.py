from django.contrib import admin
from .models import Producto, Categoria, Marca, Caracteristica, ProductoCaracteristica

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Caracteristica)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'categoria', 'marca')
    search_fields = ('codigo', 'nombre')
    list_filter = ('categoria', 'marca')

@admin.register(ProductoCaracteristica)
class ProductoCaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'caracteristica', 'valor')