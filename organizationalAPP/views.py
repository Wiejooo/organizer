from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from organizationalAPP.forms import AddForm
from organizationalAPP.models import Clothes


class MainView(TemplateView):
    """Główna strona"""

    template_name = "main_page.html"


class WardrobeView(ListView):
    """Strona szafy"""

    model = Clothes
    template_name = "wardrobe.html"
    context_object_name = "clothes"


class ClothDetailView(DetailView):
    """Szczegóły ubrania"""

    model = Clothes
    template_name = "detail.html"
    context_object_name = "cloth"


class AddClothView(CreateView):
    """Dodanie ubrania"""

    model = Clothes
    template_name = "add.html"
    form_class = AddForm
    success_url = "/notebook/wardrobe"


class ClothEditView(UpdateView):
    """Edycja ubrania"""

    model = Clothes
    template_name = "edit.html"
    fields = ["name", "size"]
    success_url = "/notebook/wardrobe"
