from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from .forms import ProductoForm, CaracteristicaFormSet
from .models import Producto, ProductoCaracteristica

# Función para verificar si el usuario pertenece al grupo ADMIN_PRODUCTS
def is_admin_products(user):
    return user.groups.filter(name='ADMIN_PRODUCTS').exists()

@login_required
def base_view(request):
    """Vista para renderizar la página base después del inicio de sesión."""
    return render(request, 'base.html')

@login_required
def registro_producto(request):
    """Vista para registrar un nuevo producto."""
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        formset = CaracteristicaFormSet(request.POST, prefix='caracteristicas')
        if form.is_valid() and formset.is_valid():
            producto = form.save()
            for caracteristica_form in formset:
                if caracteristica_form.cleaned_data:
                    caracteristica = caracteristica_form.cleaned_data['caracteristica']
                    ProductoCaracteristica.objects.create(
                        producto=producto,
                        caracteristica=caracteristica,
                        valor="N/A"
                    )
            return render(request, 'resultado.html', {'producto': producto})
    else:
        form = ProductoForm()
        formset = CaracteristicaFormSet(prefix='caracteristicas')
    return render(request, 'registro.html', {
        'form': form,
        'formset': formset
    })

@login_required
def consulta_productos(request):
    """Vista para consultar productos con todas sus características."""
    productos = Producto.objects.prefetch_related('productocaracteristica_set__caracteristica').all()
    return render(request, 'consulta.html', {'productos': productos})

@login_required
@user_passes_test(is_admin_products)
def agregar_producto(request):
    """Vista para agregar un nuevo producto (restringido a ADMIN_PRODUCTS)."""
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

@login_required
@user_passes_test(is_admin_products)
def actualizar_producto(request, producto_id):
    """Vista para actualizar un producto existente (restringido a ADMIN_PRODUCTS)."""
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('consulta_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'actualizar_producto.html', {'form': form})

@login_required
@user_passes_test(is_admin_products)
def eliminar_producto(request, producto_id):
    """Vista para eliminar un producto (restringido a ADMIN_PRODUCTS)."""
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('consulta_productos')

@login_required
def logout_view(request):
    """Vista personalizada para cerrar sesión."""
    logout(request)
    return redirect('login')