from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    def clean_rate(self):
        rate = self.cleaned_data['rate']
        if rate < 0 or rate > 10:
            raise forms.ValidationError('Рейтинг должен быть от 0 до 10')
        return rate

    class Meta:
        model = Book
        fields = '__all__'
