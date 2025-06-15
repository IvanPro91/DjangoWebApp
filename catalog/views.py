from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    DeleteView,
    UpdateView,
)

from catalog.forms import ProductForm, ModerationProductForm, ProductsModeratorForm
from catalog.models import Product, Category
from catalog.services import get_list_products


class HomePageView(ListView):
    """
    Уровень представления домашней страницы :model:'Product'

    **Шаблон:**
    :template:'templates/catalog/product_list.html'
    """
    model = Product

    def get_queryset(self):
        cache_key = 'products_list_ids'
        product_ids = cache.get(cache_key)

        if not product_ids:
            queryset = super().get_queryset().values_list('id', flat=True)
            product_ids = list(queryset)
            cache.set(cache_key, product_ids, 60 * 15)

        return Product.objects.filter(id__in=product_ids).select_related('category', 'owner')


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    """
    Уровень представления просмотра деталей продукта :model:'Product'

    **Шаблон:**
    :template:'templates/catalog/product_detail.html'
    """
    model = Product
    template_name = "catalog/product_detail.html"


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

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        return super().form_valid(form)

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

class ListProductsCategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/products_by_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_id = self.kwargs.get('pk')
        context["categories"] = get_list_products(cat_id)
        return context

    def get_queryset(self):
        queryset = cache.get('list_products')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('list_products', queryset, 60 * 15)  # Кешируем данные на 15 минут
        return queryset