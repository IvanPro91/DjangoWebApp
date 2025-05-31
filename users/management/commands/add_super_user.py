from django.core.management import BaseCommand, call_command
from catalog.models import Product, Category
from users.models import User


class Command(BaseCommand):
    help = "Добавление Супер пользователя"

    def handle(self, *args, **kwargs):
        user = User.objects.create(email = 'ivan-don4encko@ya.ru')
        user.set_password("1234")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()