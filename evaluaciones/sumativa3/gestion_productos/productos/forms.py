from django import forms
from .models import Producto, Caracteristica

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'precio', 'categoria', 'marca']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
        }

class CaracteristicaProductoForm(forms.Form):
    caracteristica = forms.ModelChoiceField(
        queryset=Caracteristica.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

CaracteristicaFormSet = forms.formset_factory(CaracteristicaProductoForm, extra=1)