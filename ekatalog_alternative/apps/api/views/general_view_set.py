from ekatalog_alternative.apps.api.filters.general_filter import GeneralFilter
from ekatalog_alternative.apps.base.models.general import General
from rest_framework import permissions, viewsets
from ekatalog_alternative.apps.api.serializers.general_serializer import GeneralSerializer
from django_filters.rest_framework import DjangoFilterBackend


class GeneralViewSet(viewsets.ModelViewSet):
    """
    API endpoint для работы с товарами с поддержкой фильтрации.

    Поддерживаемые фильтры:
    - min_price, max_price: фильтрация по цене со скидкой
    - min_rating, max_rating: фильтрация по рейтингу
    - min_reviews, max_reviews: фильтрация по количеству отзывов
    - category: точное совпадение категории (без учета регистра)
    - title: поиск по названию (частичное совпадение)

    Примеры запросов:
    - GET /api/products/?min_price=5000&min_rating=4
    - GET /api/products/?category=laptops&max_price=30000
    - GET /api/products/?min_reviews=100&title=ноутбук
    """

    queryset = General.objects.all().order_by('-created')
    serializer_class = GeneralSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Подключение фильтрации
    filter_backends = [DjangoFilterBackend]
    filterset_class = GeneralFilter

    def get_queryset(self):
        """Оптимизированный queryset с исключением NULL значений для фильтрации"""
        queryset = super().get_queryset()

        # Если есть фильтры по рейтингу, исключаем NULL значения
        if self.request.query_params.get('min_rating') or self.request.query_params.get('max_rating'):
            queryset = queryset.exclude(rating__isnull=True)

        # Если есть фильтры по отзывам, исключаем NULL значения
        if self.request.query_params.get('min_reviews') or self.request.query_params.get('max_reviews'):
            queryset = queryset.exclude(review__isnull=True)

        return queryset
