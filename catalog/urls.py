from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import ContactPageView, HomePageView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path("contacts/", ContactPageView.as_view(), name='contacts'),
    path("", HomePageView.as_view(), name='home'),
    path("details/<int:pk>", ProductDetailView.as_view(), name='details_product'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)