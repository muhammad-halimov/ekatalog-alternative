from ekatalog_alternative.apps.base.models.general import General
from django_filters import rest_framework as filters


class GeneralFilter(filters.FilterSet):
    """Фильтры для модели General"""

    # Фильтры по цене
    min_price = filters.NumberFilter(field_name="price_discount", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price_discount", lookup_expr='lte')

    # Фильтры по рейтингу
    min_rating = filters.NumberFilter(field_name="rating", lookup_expr='gte')
    max_rating = filters.NumberFilter(field_name="rating", lookup_expr='lte')

    # Фильтры по количеству отзывов
    min_reviews = filters.NumberFilter(field_name="review", lookup_expr='gte')
    max_reviews = filters.NumberFilter(field_name="review", lookup_expr='lte')

    # Дополнительные полезные фильтры
    category = filters.CharFilter(field_name="category", lookup_expr='iexact')
    title = filters.CharFilter(field_name="title", lookup_expr='icontains')

    class Meta:
        model = General
        fields = [
            'min_price', 'max_price',
            'min_rating', 'max_rating',
            'min_reviews', 'max_reviews',
            'category', 'title'
        ]