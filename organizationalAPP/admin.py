from django.contrib import admin

from organizationalAPP import models
from organizationalAPP.models import Clothes


@admin.register(models.Clothes)
class ClothesAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'brand', 'size', 'description', 'when_both', 'photo']
    list_display = ['name', 'brand', 'size']
    list_filter = ['brand']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',), }
