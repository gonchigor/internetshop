from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=False, label="Имя")
    last_name = forms.CharField(max_length=150, required=False, label="Фамилия")
    avatar = forms.ImageField(required=False, label="Аватар")
    phone = forms.CharField(max_length=15, label="Телефон")
    home_country = forms.CharField(label='домашний адрес - страна', max_length=50, required=False)
    home_city = forms.CharField(label='домашний адрес - город', max_length=50, required=False)
    home_index = forms.CharField(label='домашний адрес - индекс', max_length=15, required=False)
    home_adress1 = forms.CharField(label='домашний адрес - адрес1', required=False, widget=forms.Textarea)
    home_adress2 = forms.CharField(label='домашний адрес - адрес2', required=False, widget=forms.Textarea)
    dop_info = forms.CharField(label='дополнительная информация', required=False, widget=forms.Textarea)
