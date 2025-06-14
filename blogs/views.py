from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)

from blogs.forms import BlogsForm, ModerationBlogsForm
from blogs.models import Blogs


class BlogCreateView(CreateView):
    """
    Уровень представления создания блога :model:'Blogs'

    **Шаблон:**
    :template:'templates/blogs/blogs_form.html'
    """
    model = Blogs
    form_class = BlogsForm
    success_url = reverse_lazy("blogs:home_blogs")


class BlogDetailsView(DetailView):
    """
    Уровень представления просмотра деталей блога :model:'Blogs'

    **Шаблон:**
    :template:'templates/blogs/blogs_detail.html'
    """
    model = Blogs
    form_class = BlogsForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if self.request.user == self.object.owner:
            obj.views += 1
            obj.save()
            return obj
        return HttpResponseForbidden

class BlogUpdateView(UpdateView):
    """
    Уровень представления обновления блога :model:'Blogs'

    **Шаблон:**
    :template:'templates/blogs/blogs_form.html'
    """
    model = Blogs
    form_class = BlogsForm
    success_url = reverse_lazy("blogs:home_blogs")


class BlogDeleteView(DeleteView):
    """
    Уровень представления подтверждения удаления блога :model:'Blogs'

    **Шаблон:**
    :template:'templates/blogs/blogs_confirm_delete.html'
    """
    model = Blogs
    success_url = reverse_lazy("blogs:home_blogs")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return BlogsForm
        raise PermissionDenied


class BlogsListView(ListView):
    """
    Уровень представления показа списка блогов :model:'Blogs'

    **Шаблон:**
    :template:'templates/blogs/blogs_list.html'
    """
    model = Blogs
    form_class = BlogsForm

    def get_queryset(self):
        return Blogs.objects.filter(publication=True)
