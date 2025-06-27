from django.db import models


class Shop(models.Model):
    title = models.CharField(
        max_length=32,
        null=True,
        verbose_name='Наименование'
    )
    address = models.CharField(
        max_length=255,
        null=True,
        verbose_name='Адрес'
    )
    url = models.URLField(
        null=True,
        verbose_name='Ссылка на сайт'
    )
    image = models.URLField(
        null=True,
        blank=True,
        default="assets/img/icons/default_product.svg",
        verbose_name='Фото магазина'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание'
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
        'address',
        'url',
        'image',
        'description',
        'created',
        'updated',
    ]
    SearchableFields = [
        'id',
        'title',
        'address',
        'url',
        'image',
        'description',
        'created',
        'updated',
    ]
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['-id', '-updated']
        verbose_name = 'магазин'
        verbose_name_plural = 'магазины'

    def __str__(self):
        return self.title or self.id
