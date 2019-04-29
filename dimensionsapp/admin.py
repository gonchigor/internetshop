from django.contrib import admin
from .models import *

# Register your models here.
class ModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Author, ModelAdmin)
admin.site.register(Serie, ModelAdmin)
admin.site.register(Jenre, ModelAdmin)
admin.site.register(PublishingHouse, ModelAdmin)
admin.site.register(Binding)
admin.site.register(FormatBook)
admin.site.register(AgeRestriction, ModelAdmin)