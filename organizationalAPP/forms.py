from django import forms
from django.forms import ModelForm

from organizationalAPP.models import Clothes


class ClothesForm(ModelForm):
    class Meta:
        model = Clothes
        fields = ['name', 'brand', 'size', 'description', 'when_both', 'photo']


class AddForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ('name', 'brand', 'size', 'description', 'when_both', 'photo')
