import django_filters


class FiltroPrecoFilterSet(django_filters.FilterSet):
    preco_min = django_filters.NumberFilter(
        field_name="preco", lookup_expr="gte", label="Preço Mínimo"
    )
    preco_max = django_filters.NumberFilter(
        field_name="preco", lookup_expr="lte", label="Preço Máximo"
    )
