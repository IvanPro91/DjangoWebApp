from django.forms import ModelForm

from blogs.models import Blogs


class BlogsForm(ModelForm):
    class Meta:
        model = Blogs
        fields = "__all__"

    def __init__(self, *args, **kwargs):
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
