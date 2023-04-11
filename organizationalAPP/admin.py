from django.contrib import admin

from organizationalAPP import models


@admin.register(models.Clothes)
class ClothesAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'brand', 'size', 'description', 'photo']
    list_display = ['name', 'brand', 'size']
    list_filter = ['brand']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',), }
