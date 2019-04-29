from django import forms
from .models import Author, Jenre, PublishingHouse, Serie, FormatBook, Binding, AgeRestriction


class SearchForm(forms.Form):
    search = forms.CharField(label='Наименование', required=False)


class SearchFormAuthor(forms.Form):
    search = forms.CharField(label='Имя', required=False)


class AuthorModel(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class JenreModel(forms.ModelForm):
    class Meta:
        model = Jenre
        fields = '__all__'


class PublishingHouseModel(forms.ModelForm):
    class Meta:
        model = PublishingHouse
        fields = '__all__'


class SerieModel(forms.ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'


class FormatBookModel(forms.ModelForm):
    class Meta:
        model = FormatBook
        fields = '__all__'


class BindingModel(forms.ModelForm):
    class Meta:
        model = Binding
        fields = '__all__'


class AgeRestrictionModel(forms.ModelForm):
    class Meta:
        model = AgeRestriction
        fields = '__all__'
