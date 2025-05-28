from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import ContactPageView, HomePageView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    path("contacts/", ContactPageView.as_view(), name='contacts'),
    path("", HomePageView.as_view(), name='home'),
    path("create_product/", ProductCreateView.as_view(), name='create_product'),
    path("update_product/<int:pk>/update/", ProductUpdateView.as_view(), name='update_product'),
    path("delete_product/<int:pk>/delete/", ProductDeleteView.as_view(), name='delete_product'),
    path("details/<int:pk>", ProductDetailView.as_view(), name='details_product'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
