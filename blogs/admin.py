from django.contrib import admin
from blogs.models import Blogs


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    """
    Регистрация модели :model:'Blogs' в кабинете администратора
    """
    list_display = (
        "id",
        "title",
        "content",
        "image",
        "created_at",
        "publication",
        "views",
    )
    list_filter = ("title",)
    search_fields = ("title", "publication")
