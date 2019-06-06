from django import forms
from .models import BookInCart


class AddBookToCartForm(forms.ModelForm):
    url = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = BookInCart
        fields = ['quantity', 'book']
        widgets = {'book': forms.HiddenInput}

    def clean(self):
        cleaned_data = super().clean()
        book = cleaned_data.get("book")
        quantity = cleaned_data.get("quantity")

        if book and quantity:
            if not book.is_active:
                raise forms.ValidationError("Книга не доступна для заказа")
            if quantity > book.count_books:
                raise forms.ValidationError(f"Доступно только {book.count_books} книг")
            # Only do something if both fields are valid so far.
            # if "help" not in subject:
            #     raise forms.ValidationError(
            #         "Did not send for 'help' in the subject despite "
            #         "CC'ing yourself."
            #     )
