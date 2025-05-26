from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def view_page_home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})

def view_page_contacts(request):
    return render(request, "contacts.html")

def view_detail_product(request, id_product):
    product = get_object_or_404(Product, pk=id_product)
    return render(request, "details_product.html", {"product": product})