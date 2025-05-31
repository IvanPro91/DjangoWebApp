from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)

from blogs.forms import BlogsForm
from blogs.models import Blogs


class BlogCreateView(CreateView):
    model = Blogs
    form_class = BlogsForm
    success_url = reverse_lazy("blogs:home_blogs")


class BlogDetailsView(DetailView):
    model = Blogs
    form_class = BlogsForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj


class BlogUpdateView(UpdateView):
    model = Blogs
    form_class = BlogsForm
    success_url = reverse_lazy("blogs:home_blogs")


class BlogDeleteView(DeleteView):
    model = Blogs
    success_url = reverse_lazy("blogs:home_blogs")


class BlogsListView(ListView):
    model = Blogs
    form_class = BlogsForm

    def get_queryset(self):
        return Blogs.objects.filter(publication=True)
