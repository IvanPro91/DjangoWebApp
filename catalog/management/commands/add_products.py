from django.core.management import BaseCommand, call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Добавление тестовых данных с фикстуры"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        call_command("loaddata", "catalog.json")
        self.stdout.write(self.style.SUCCESS("Выполнено успешно"))
