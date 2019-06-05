from django import forms
from dimensionsapp.models import Jenre, PublishingHouse


class JenreNavForm(forms.Form):
    jenre_list = Jenre.objects.all().values_list('pk', 'name')
    publishing_list = PublishingHouse.objects.all().values_list('pk', 'name')
    search = forms.CharField(label='Поиск:', required=False)
    active = forms.BooleanField(label='На складе', required=False)
    j = forms.MultipleChoiceField(choices=jenre_list, widget=forms.CheckboxSelectMultiple, label="Жанр", required=False)
    p = forms.MultipleChoiceField(choices=publishing_list, widget=forms.CheckboxSelectMultiple,
                                  label="Издательство", required=False)
