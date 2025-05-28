from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product

class HomePageView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ContactPageView(TemplateView):
    template_name = "contacts.html"

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")