from django.contrib import admin
from . import models
# Register your models here.


class CartAdmin(admin.ModelAdmin):

    list_display = ['user', 'date_create', 'date_update']
    list_display_links = ['user']
    readonly_fields = ['date_create', 'date_update']


class BookInCartAdmin(admin.ModelAdmin):

    list_display = ['cart', 'book', 'quantity', 'date_create', 'date_update']
    readonly_fields = ['date_create', 'date_update']


admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.BookInCart, BookInCartAdmin)
