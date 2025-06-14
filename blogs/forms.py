from django.forms import ModelForm

from blogs.models import Blogs


class ModerationBlogsForm(ModelForm):
    """
    Форма отображения данных :model:'Blogs'
    fields:
        Отображение колонок в форме __all__ - все
    """
    class Meta:
        model = Blogs
        fields = "__all__"


class BlogsForm(ModelForm):
    """
    Форма отображения данных :model:'Blogs'
    fields:
        Отображение колонок в форме __all__ - все
    """
    class Meta:
        model = Blogs
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Формирование классов фреймворка для полей БД
        """
        super(BlogsForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название блога"}
        )

        self.fields["content"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание"}
        )

        self.fields["views"].widget.attrs.update(
            {"class": "form-control", "type": "number"}
        )
