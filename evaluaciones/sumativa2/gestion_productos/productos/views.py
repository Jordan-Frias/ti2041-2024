from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm, CaracteristicaFormSet
from .models import Producto, ProductoCaracteristica

@login_required
def registro_producto(request):
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
    # Obtener todos los productos con sus características       
    productos = Producto.objects.prefetch_related('productocaracteristica_set__caracteristica').all()
    return render(request, 'consulta.html', {'productos': productos})
