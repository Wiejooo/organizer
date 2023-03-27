from django.contrib import admin
from organizationalAPP.models import Clothes


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    fields = ['name', 'brand', 'size', 'description', 'when_both', 'photo']
    list_display = ['name', 'brand', 'size']
    list_filter = ['brand']
    search_fields = ['name', 'description']
