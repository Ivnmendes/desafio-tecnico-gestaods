import django_filters


class FiltroPrecoFilterSet(django_filters.FilterSet):
    preco_min = django_filters.NumberFilter()
    preco_max = django_filters.NumberFilter()
