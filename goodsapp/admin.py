from django.contrib import admin
from . import models
from django.utils.html import format_html

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if (obj.image_field == ""):
            return "Нет изображения"
        return format_html('<img src="{}" style="max-width:100px; max-height:150px;" />'.format(obj.image_field.url))

    image_tag.short_description = 'изображение'

    list_display = ['image_tag', 'description', 'date_create', 'date_update']
    list_display_links = ['description']
    readonly_fields = ['date_create', 'date_update', 'image_tag']


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Menu)
