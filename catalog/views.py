from django.shortcuts import render

def view_page_home(request):
    return render(request, "home.html")

def view_page_contacts(request):
    return render(request, "contacts.html")