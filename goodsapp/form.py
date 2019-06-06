from django import forms
from .models import Book, BookAction


class BookForm(forms.ModelForm):
    def clean_rate(self):
        rate = self.cleaned_data['rate']
        if rate < 0 or rate > 10:
            raise forms.ValidationError('Рейтинг должен быть от 0 до 10')
        return rate

    class Meta:
        model = Book
        fields = '__all__'


class BookModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.description()


class BookActionForm(forms.ModelForm):
    book = BookModelChoiceField(queryset=Book.objects.all())

    class Meta:
        model = BookAction
        fields = '__all__'


class BookLoadForm(forms.Form):
    file = forms.FileField(label="Файл csv")
