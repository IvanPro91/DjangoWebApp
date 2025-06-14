from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    DeleteView,
    UpdateView,
)

from catalog.forms import ProductForm, ModerationProductForm, ProductsModeratorForm
from catalog.models import Product


class HomePageView(ListView):
    """
    Уровень представления домашней страницы :model:'Product'

    **Шаблон:**
    :template:'templates/catalog/product_list.html'
    """
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    """
    Уровень представления просмотра деталей продукта :model:'Product'

    **Шаблон:**
    :template:'templates/catalog/product_detail.html'
    """
    model = Product



class ContactPageView(LoginRequiredMixin, TemplateView):
    """
    Уровень представления страницы контактов

    **Шаблон:**
    :template:'templates/contacts.html'
    """
    template_name = "contacts.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Уровень представления создания нового продукта :model:'Product'

    **Шаблон:**
    :template:'templates/catalog/product_form.html'
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Уровень представления удаления продукта :model:'Product'

    **Шаблон:**
    :template:'templates/catalog/product_congirm_delete.html'
    """
    model = Product
    success_url = reverse_lazy("catalog:home")
    permission_required = 'catalog.can_unpublish_product'

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("can_delete_product"):
            return ModerationProductForm
        raise PermissionDenied

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    Уровень представления обновления продукта :model:'Product'

    **Шаблон:**
    :template:'templates/catalog/product_form.html'
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_form_class(self):
        user = self.request.user

        if user == self.object.owner:
            return ProductForm
        if user.has_perm('can_unpublish_product'):
            return ProductsModeratorForm
        raise PermissionDenied