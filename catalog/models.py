from django.db import models

from users.models import User


class Category(models.Model):
    """
    Модель для хранения информации о группах продуктов.
    Meta:
        verbose_name (str): Отображаемое имя модели в единственном числе (Категория).
        verbose_name_plural (str): Отображаемое имя модели во множественном числе (Категории).
    """
    name = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="наименование"
    )
    description = models.TextField(blank=True, null=True, verbose_name="описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    """
    Модель для хранения информации о продукте. Связана с :model:'catalog.Category'.
    Meta:
        verbose_name (str): Отображаемое имя модели в единственном числе (Продукт).
        Verbose_name_plural (str): Отображаемое имя модели во множественном числе (Продукты).
    """
    name = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="наименование"
    )
    description = models.TextField(blank=True, null=True, verbose_name="описание")
    image = models.ImageField(
        upload_to="products/images", blank=True, null=True, verbose_name="изображение"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="категория",
    )
    price = models.PositiveIntegerField(
        blank=False, null=False, verbose_name="цена за покупку"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="дата последнего изменения"
    )
    owner = models.ForeignKey(User, verbose_name='Владелец', blank=True, null=True, help_text='Введите владельца', on_delete=models.CASCADE)

    PUBLIC_STATUS = [
        ('public', 'Опубликовано'),
        ('unpublic', 'Не опубликовано')
    ]
    status = models.CharField(
        max_length=20,
        choices=PUBLIC_STATUS,
        default='unpublic',
        verbose_name='Статус публикации'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [
            ("can_unpublish_product", "Право на публикацию товара"),
            ("can_delete_product", "Право на удаление продукта"),
        ]
