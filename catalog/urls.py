from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import view_page_home, view_page_contacts

app_name = 'catalog'

urlpatterns = [
    path("contacts/", view_page_contacts, name='contacts'),
    path("", view_page_home, name='home'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)