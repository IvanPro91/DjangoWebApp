from django.urls import path

from catalog.views import view_page_home, view_page_contacts

urlpatterns = [
    path("contacts/", view_page_contacts),
    path("home/", view_page_home),
    path("/", view_page_home),
    path("", view_page_home),
]

