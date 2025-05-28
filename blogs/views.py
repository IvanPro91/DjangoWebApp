from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from blogs.models import Blogs


class BlogCreateView(CreateView):
    model = Blogs
    fields = ("title", "content", "image", "publication")
    success_url = reverse_lazy("blogs:home_blogs")

class BlogDetailsView(DetailView):
    model = Blogs

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj


class BlogUpdateView(UpdateView):
    model = Blogs
    fields = ("title", "content", "image", "publication")
    success_url = reverse_lazy("blogs:home_blogs")

class BlogDeleteView(DeleteView):
    model = Blogs
    success_url = reverse_lazy("blogs:home_blogs")

class BlogsListView(ListView):
    model = Blogs

    def get_queryset(self):
        return Blogs.objects.filter(publication = True)