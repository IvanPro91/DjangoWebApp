from django.contrib import admin
from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Регистрация модели :model:'Product' в кабинете администратора
    """
    list_display = (
        "id",
        "name",
        "price",
        "category",
    )
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Регистрация модели :model:'Category' в кабинете администратора
    """
    list_display = (
        "id",
        "name",
    )
