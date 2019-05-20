from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from .models import Order
# from django import forms


class OrderConfirmForm(ModelForm):
    # def clean_phone(self):
    #     phone = self.cleaned_data['phone']
    #     if not phone.startswith('+375'):
    #         raise forms.ValidationError('Номер должен начинаться с +375')
    #     return phone

    class Meta:
        model = Order
        # fields = '__all__'
        exclude = ['cart', 'status']
        # widgets = {
        #     'cart': HiddenInput,
        #     'status': HiddenInput
        # }
