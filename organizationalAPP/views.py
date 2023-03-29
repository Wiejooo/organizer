from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, FormView

from organizationalAPP.forms import AddForm
from organizationalAPP.models import Clothes


class MainView(View):
    template_name = 'main_page.html'

    def get(self, request):
        return render(request, self.template_name)


class WardrobeView(ListView):
    model = Clothes
    template_name = 'wardrobe.html'
    context_object_name = 'cloth'


class AddClothView(FormView):
    template_name = 'add.html'
    form_class = AddForm
    success_url = '../wardrobe/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

