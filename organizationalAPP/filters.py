import django_filters
from django import forms

from organizationalAPP.models import Clothes, ClothType

x = ClothType.type


FILTER_CHOICES = (
    x
)
class ProductFilter(django_filters.FilterSet):
    """Filtrowanie obiektów"""

    cloth_type = django_filters.ChoiceFilter(choices=FILTER_CHOICES)
    class Meta:
        model = Clothes
        fields = {
            'name': ['icontains'],
            'brand': ['icontains'],
        }