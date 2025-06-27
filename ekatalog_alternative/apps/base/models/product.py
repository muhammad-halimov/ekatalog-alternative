from django.db import models
from .category import Category
from .shop import Shop


class Product(models.Model):
    title = models.CharField(
        max_length=32,
        null=True,
        verbose_name='Наименование'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Категория'
    )
    shop = models.ForeignKey(
        Shop,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Магазин'
    )
    price = models.DecimalField(
        null=True,
        decimal_places=2,
        max_digits=11,
        verbose_name='Цена'
    )
    url = models.URLField(
        null=True,
        verbose_name='Ссылка на товар'
    )
    brand = models.CharField(
        max_length=32,
        null=True,
        verbose_name='Производитель'
    )
    model = models.CharField(
        max_length=32,
        null=True,
        verbose_name='Модель'
    )
    specifications = models.JSONField(
        null=True,
        blank=True,
        verbose_name='Характеристики'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    image = models.URLField(
        null=True,
        blank=True,
        default="assets/img/icons/default_product.svg",
        verbose_name='Фото продукта'
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
        'title',
        'category',
        'shop',
        'brand',
        'model',
        'price',
        'created',
        'updated',
    ]
    SearchableFields = [
        'id',
        'title',
        'description',
        'brand',
        'model',
        'image',
        'price',
        'url',
        'created',
        'updated',
    ]
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['-id', '-updated']
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.title or self.id
