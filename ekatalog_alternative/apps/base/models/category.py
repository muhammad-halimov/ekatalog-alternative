from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=32,
        null=True,
        verbose_name='Наименование'
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
        'description',
        'created',
        'updated',
    ]
    SearchableFields = [
        'id',
        'title',
        'description',
        'created',
        'updated',
    ]
    FilterFields = ['created', 'updated']

    class Meta:
        ordering = ['-id', '-updated']
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title or self.id
