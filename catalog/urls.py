from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (
    ContactPageView,
    HomePageView,
    get_feedback,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView, ListProductsCategoryDetailView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("get_feedback/", get_feedback, name="feedback"),
    path("contacts/", ContactPageView.as_view(), name="contacts"),
    path("", HomePageView.as_view(), name="home"),
    path("create_product/", ProductCreateView.as_view(), name="create_product"),
    path("catalog/<int:pk>/", ListProductsCategoryDetailView.as_view(), name="catalog_product"),
    path("update_product/<int:pk>/update/", ProductUpdateView.as_view(), name="update_product"),
    path("delete_product/<int:pk>/delete/", ProductDeleteView.as_view(), name="delete_product"),
    path("details/<int:pk>", ProductDetailView.as_view(), name="details_product")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
