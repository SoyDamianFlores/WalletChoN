# En billetera/forms.py
from django import forms
from .models import Usuario


class BilleteraForm(forms.Form):
    ingresos_mensuales = forms.DecimalField(label='ingresos_mensuales', max_digits=10, decimal_places=0)
    gasto_alquiler = forms.DecimalField(label='Alquiler', max_digits=10, decimal_places=0)
    gasto_comida = forms.DecimalField(label='Comida', max_digits=10, decimal_places=0)
    gasto_transporte = forms.DecimalField(label='Transporte', max_digits=10, decimal_places=0)
    gasto_telefonia = forms.DecimalField(label='Telefonía', max_digits=10, decimal_places=0)
    gasto_gimnasio = forms.DecimalField(label='Gimnasio', max_digits=10, decimal_places=0)
    gasto_fiestas = forms.DecimalField(label='Fiestas', max_digits=10, decimal_places=0)
    gasto_restaurant = forms.DecimalField(label='Restaurant', max_digits=10, decimal_places=0)
    gasto_shopping = forms.DecimalField(label='Shopping', max_digits=10, decimal_places=0)
    gasto_otros = forms.DecimalField(label='Otros', max_digits=10, decimal_places=0)
    
    # Agrega el campo porcentaje_ahorro
    porcentaje_ahorro = forms.DecimalField(label='porcentaje_ahorro', max_digits=5, decimal_places=0)

