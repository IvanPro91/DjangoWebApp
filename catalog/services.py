from catalog.models import Product

def get_list_products(category_pk):
    return Product.objects.filter(category=category_pk)