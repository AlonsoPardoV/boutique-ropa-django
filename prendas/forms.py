from django import forms
from .models import Prenda


class PrendaForm(forms.ModelForm):
    class Meta:
        model = Prenda
        fields = [
            'nombre',
            'categoria',
            'talla',
            'color',
            'precio',
            'stock',
            'marca',
            'descripcion',
        ]