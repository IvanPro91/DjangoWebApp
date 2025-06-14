from django.forms import ModelForm
from catalog.models import Product



class ModerationProductForm(ModelForm):
    """
    Форма модератора отображения в html :model:'Product'
    Meta:
        fields - отображение колонок
    """
    class Meta:
        model = Product
        fields = ("name", "description")


class ProductsModeratorForm(ModelForm):
    """
    Форма формирования отображения в html :model:'Product'
    Meta:
        fields - отображение колонок
    """
    class Meta:
        model = Product
        fields = ("status",)


class ProductForm(ModelForm):
    """
    Форма формирования отображения в html :model:'Product'
    Meta:
        fields - отображение колонок
    """
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Формирование классов фреймворка для полей БД
        """
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите наименование товара"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание"}
        )

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-select",
            }
        )

        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "type": "number"}
        )

    def clean_price(self):
        """
        Проверка поля price(цена) на условие > 0
        """
        price = self.cleaned_data.get("price")
        if price and price < 0:
            self.add_error("price", f"Цена не может быть меньше 0")
        return price

    def clean(self):
        """
        Получение значения name и проверка на отсутствие слов которые не должны попасть в форму
        """
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        word_valid = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        if name and name in word_valid:
            self.add_error("name", f'Name не может содержать слово "{name}"')
