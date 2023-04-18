from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from organizationalAPP.forms import AddForm, AddTypeForm
from organizationalAPP.models import Clothes, ClothType
from organizationalAPP.forms import ClothesForm


class MainView(TemplateView):
    """Główna strona"""

    template_name = "main_page.html"


class WardrobeView(ListView):
    """Strona szafy"""

    model = Clothes
    template_name = "wardrobe.html"
    context_object_name = "clothes"

    # Przekazywanie wartości do template (zostawiłem może na później)
    # def get_context_data(self, **kwargs):
    #         context = super(WardrobeView, self).get_context_data(**kwargs)
    #         context.update({'switch_view': self.switch_view})
    #         return context

class WardrobeTableView(ListView):
    """Strona szafy"""

    model = Clothes
    template_name = "wardrobe_table.html"
    context_object_name = "clothes"

class ClothDetailView(DetailView):
    """Szczegóły ubrania"""

    model = Clothes
    template_name = "detail.html"
    context_object_name = "cloth"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class AddClothView(CreateView):
    """Dodanie ubrania"""

    model = Clothes
    template_name = "add.html"
    form_class = AddForm
    success_url = "/notebook/wardrobe"


class AddTypeView(CreateView):
    """Dodanie typu ubrań"""

    model = ClothType
    template_name = 'add_cloth_type.html'
    form_class = AddTypeForm
    success_url = "/notebook/wardrobe"

class ClothEditView(UpdateView):
    """Edycja ubrania"""

    model = Clothes
    template_name = "edit.html"
    form_class = ClothesForm
    success_url = "/notebook/wardrobe"

class ClothDeleteView(DeleteView):
    """Usunięcie ubrania"""

    model = Clothes
    template_name = 'delete_cloth.html'
    success_url = '/notebook/wardrobe'

