from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
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
        price = self.cleaned_data.get("price")
        if price and price < 0:
            self.add_error("price", f"Цена не может быть меньше 0")
        return price

    def clean(self):
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
