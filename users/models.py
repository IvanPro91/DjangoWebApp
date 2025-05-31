from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    avatar = models.ImageField(upload_to="avatar/users", blank=True, null=True, verbose_name="аватар")
    phone = models.CharField(max_length=35, blank=True, null=True, verbose_name="телефон", help_text="Введите номер телефона")
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name="почта", help_text="Введите почту")
    city = models.TextField(blank=False, null=False, verbose_name="страна", help_text="Введите страну")
    token = models.CharField(max_length=100, blank=True, verbose_name="Токен")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    AUTH_USER_MODEL = "users.User"