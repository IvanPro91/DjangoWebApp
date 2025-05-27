from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product

class HomePageView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ContactPageView(TemplateView):
    template_name = "contacts.html"
