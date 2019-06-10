from django import forms
from dimensionsapp.models import Jenre, PublishingHouse, Serie


class ModelMultipleChoiceFieldByName(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class JenreNavForm(forms.Form):
    # jenre_list = Jenre.objects.all().values_list('pk', 'name')
    # publishing_list = PublishingHouse.objects.all().values_list('pk', 'name')
    # serie_list = Serie.objects.all().values_list('pk', 'name')
    search = forms.CharField(label='Поиск:', required=False)
    active = forms.BooleanField(label='На складе', required=False)
    j = ModelMultipleChoiceFieldByName(
        queryset=Jenre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Жанр",
        required=False
    )
    p = ModelMultipleChoiceFieldByName(
        queryset=PublishingHouse.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Издательство",
        required=False
    )
    s = ModelMultipleChoiceFieldByName(
        queryset=Serie.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Серия",
        required=False
    )
