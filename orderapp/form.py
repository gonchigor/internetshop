from django.forms import ModelForm, widgets, ValidationError
from django.forms.widgets import HiddenInput
from .models import Order
from dimensionsapp.models import OrderStatus

order_status_cancel_customer = OrderStatus.objects.get_or_create(name='Отменен покупателем')[0]
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


class OrderCancelForm(ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        widgets = {'status': widgets.HiddenInput}

    def clean_status(self):
        status = self.cleaned_data['status']
        if status.pk != order_status_cancel_customer.pk:
            raise ValidationError("Status is not cancel by customer!!!")
        return status


class OrderCustomerCommentForm(ModelForm):
    class Meta:
        model = Order
        fields = ['comments']
