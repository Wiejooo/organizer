from django.contrib import admin

from organizationalAPP import models


@admin.register(models.Clothes)
class ClothesAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'brand', 'size', 'description', 'photo', 'cloth_type', 'cloth_sub_type' ,'sell_statute']
    list_display = ['name', 'brand', 'size']
    list_filter = ['brand']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',), }


@admin.register(models.ClothType)
class ClothTypesAdmin(admin.ModelAdmin):
    fields = ['type', 'measurement']


@admin.register(models.Marketplaces)
class MarketplacesAdmin(admin.ModelAdmin):
    fields = ['name']


@admin.register(models.Sizes)
class SizeAdmin(admin.ModelAdmin):
    fields = ['type']
