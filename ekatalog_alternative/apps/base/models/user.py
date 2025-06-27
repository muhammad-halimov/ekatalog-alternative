from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=32,
        null=True,
        verbose_name='Логин'
    )
    name = models.CharField(
        max_length=32,
        null=True,
        verbose_name='Имя'
    )
    surname = models.CharField(
        max_length=32,
        null=True,
        verbose_name='Фамилия'
    )
    patronymic = models.CharField(
        max_length=23,
        null=True,
        verbose_name='Отчество'
    )
    email = models.EmailField(
        unique=True,
        null=True,
        verbose_name='Почта'
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        default="assets/img/icons/avatar.svg",
        verbose_name='Аватар'
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
        'username',
        'name',
        'surname',
        'patronymic',
        'email',
        'avatar',
        'created',
        'updated',
    ]
    SearchableFields = [
        'id',
        'username',
        'name',
        'surname',
        'patronymic',
        'email',
        'avatar',
        'created',
        'updated',
    ]
    FilterFields = ['created', 'updated']

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        app_label = 'base'
        verbose_name = 'пользователя'
        verbose_name_plural = 'пользователи'
        ordering = ['-id', '-updated']

    def __str__(self):
        return self.username or self.email
