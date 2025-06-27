from django.db import models
from .category import Category
from .shop import Shop


class General(models.Model):
    wb_id = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Арт. WB'
    )
    title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name='Наименование'
    )
    category = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name='Категория'
    )
    price_discount = models.DecimalField(
        null=True,
        blank=True,
        max_digits=11,
        decimal_places=2,
        verbose_name='Со скидкой'
    )
    price_original = models.DecimalField(
        null=True,
        blank=True,
        max_digits=11,
        decimal_places=2,
        verbose_name='Без скидки'
    )
    rating = models.DecimalField(
        null=True,
        blank=True,
        max_digits=3,
        decimal_places=2,
        verbose_name='Оценка'
    )
    review = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Отзывов'
    )
    link = models.URLField(
        null=True,
        blank=True,
        verbose_name='Ссылка товара'
    )
    photo = models.URLField(
        null=True,
        blank=True,
        default="assets/img/icons/default_product.svg",
        verbose_name='Фото товара'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Обновлено'
    )

    DisplayFields = [
        'id',
        'wb_id',
        'title',
        'category',
        'price_original',
        'price_discount',
        'rating',
        'review',
        # 'link',
        # 'photo',
        'created',
        'updated',
    ]
    SearchableFields = [
        'id',
        'wb_id',
        'title',
        'category',
        'price_discount',
        'price_original',
        'rating',
        'review',
        'link',
        'photo',
        'created',
        'updated',
    ]
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = []
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.title or self.id
