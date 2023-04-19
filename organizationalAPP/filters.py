import django_filters
from django import forms

from organizationalAPP.models import Clothes, ClothType


class ProductFilter(django_filters.FilterSet):
    """Filtrowanie obiektów"""

    cloth_type = django_filters.ModelChoiceFilter(
        queryset=ClothType.objects.all(),
        label='Type',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )


    class Meta:
        model = Clothes
        fields = {
            'name': ['icontains'],
            'brand': ['icontains'],
        }