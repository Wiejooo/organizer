from typing import Any, Dict
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from organizationalAPP.forms import AddForm, AddTypeForm, AddSubTypeForm, AddMeasurementsForm
from organizationalAPP.models import Clothes, ClothType, ClothSubType, Sizes
from organizationalAPP.forms import ClothesForm
from organizationalAPP.filters import ProductFilter
from django.db.models import Sum


class MainView(ListView):
    """Główna strona"""

    model = Clothes
    template_name = "main_page.html"
    context_object_name = "clothes"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        price = Clothes.objects.aggregate(Sum("purchase_price")).get("purchase_price__sum")
        clothes = Clothes.objects.all()
        money_earned = Clothes.objects.aggregate(Sum('sold_price')).get('sold_price__sum')
        income = money_earned - price
        predicting_earnings = Clothes.objects.aggregate(Sum('predicted_sale_price')).get('predicted_sale_price__sum')
        context = {
            'price': price,
             'clothes': clothes,
             'money_earned': money_earned,
             'income': income,
             'predicting_earnings': predicting_earnings
             }
        return context

class WardrobeView(ListView):
    """Strona szafy kafelki"""

    model = Clothes
    template_name = "wardrobe.html"
    context_object_name = "clothes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ProductFilter(
            self.request.GET, queryset=self.get_queryset()
        )
        return context


class WardrobeTableView(ListView):
    """Strona szafy tabela"""

    model = Clothes
    template_name = "wardrobe_table.html"
    context_object_name = "clothes"


class ClothDetailView(DetailView):
    """Szczegóły ubrania kafelki"""

    model = Clothes
    template_name = "detail.html"
    context_object_name = "cloth"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class ClothDetailTableView(DetailView):
    """Szczegóły ubrania tabela"""

    model = Clothes
    template_name = "detail-table.html"
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
    template_name = "add_cloth_type.html"
    form_class = AddTypeForm
    success_url = "/notebook/wardrobe"


class AddSubTypeView(CreateView):
    """Dodanie sub-typu ubrań"""

    model = ClothSubType
    template_name = "add_cloth_sub_type.html"
    form_class = AddSubTypeForm
    success_url = "/notebook/wardrobe"

class AddMeasurementsView(CreateView):
    """Dodanie wymiaru ubrań"""

    model = Sizes
    template_name = "add_measurements.html"
    form_class = AddMeasurementsForm
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
    template_name = "delete_cloth.html"
    success_url = "/notebook/wardrobe"


class TypeListView(ListView):
    """Lista typów ubrać"""

    model = ClothType
    template_name = "type_list.html"
    context_object_name = "types"
