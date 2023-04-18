import django_filters

from organizationalAPP.models import Clothes

class ProductFilter(django_filters.FilterSet):
    """Filtrowanie obiektów"""

    name = django_filters.CharFilter()
    name__gt = django_filters.CharFilter(field_name='name', lookup_expr='gt')
    name__lt = django_filters.CharFilter(field_name='name', lookup_expr='lt')

    brand = django_filters.CharFilter()
    brand__gt = django_filters.CharFilter(field_name='name', lookup_expr='gt')
    brand__lt = django_filters.CharFilter(field_name='name', lookup_expr='lt')

    class Meta:
        model = Clothes
        fields = ['name', 'brand']