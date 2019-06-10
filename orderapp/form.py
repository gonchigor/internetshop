from django.forms import ModelForm, widgets, ValidationError, ModelChoiceField
from django.forms.widgets import HiddenInput
from .models import Order
from dimensionsapp.models import OrderStatus

order_status_cancel_customer = OrderStatus.objects.get_or_create(name='Отменен покупателем')[0]
# from django import forms
manger_status_list = ['Доставлен', 'Комплектуется', 'Отменен']


class OrderConfirmForm(ModelForm):
    # def clean_phone(self):
    #     phone = self.cleaned_data['phone']
    #     if not phone.startswith('+375'):
    #         raise forms.ValidationError('Номер должен начинаться с +375')
    #     return phone

    class Meta:
        model = Order
        # fields = '__all__'
        exclude = ['status']
        widgets = {
            'cart': HiddenInput,
            # 'status': HiddenInput
        }

    def clean(self):
        clean_data = super().clean()
        if 'cart' in self.changed_data:
            raise ValidationError('Не меняй HTML код!!!')
        cart = clean_data.get("cart")
        error = []
        for book_in_cart in cart.books.all():
            if not book_in_cart.book.is_active:
                error.append(f"Книга {book_in_cart.book.description()} не доступна для заказа")
            elif book_in_cart.quantity > book_in_cart.book.count_books:
                error.append(f"На складе всего {book_in_cart.book.count_books} книг {book_in_cart.book.description()}")
        if error:
            raise ValidationError(error)


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'status', 'phone', 'email', 'delivery_adress']


class OrderFieldStatusForm(ModelForm):
    status = ModelChoiceField(queryset=OrderStatus.objects.filter(name__in=manger_status_list), empty_label=None)

    class Meta:
        model = Order
        fields = ['status']
        # widgets = {'status': widgets.ChoiceWidget(choices=tuple(OrderStatus.objects.filter(
        #     pk__in=[1, 3, 4, 5]).values_list('id', 'name')))}


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
