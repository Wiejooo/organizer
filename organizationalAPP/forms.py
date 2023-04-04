from django import forms
from django.forms import ModelForm

from organizationalAPP.models import Clothes


class ClothesForm(ModelForm):
    class Meta:
        model = Clothes
        fields = ['name', 'slug', 'brand', 'size', 'description', 'when_both', 'photo']


class AddForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ('name', 'brand', 'size', 'description', 'when_both', 'photo')

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'brand': forms.TextInput(attrs={'class': 'form-control'}),
        #     'size': forms.TextInput(attrs={'class': 'form-control'}),
        #     # 'description': forms.TextInput(attrs={'class': 'form-control'}),
        #     # 'when_both': forms.TextInput(attrs={'class': 'form-control'}),
        #     # 'photo': forms.TextInput(attrs={'class': 'form-control'}),
        # }
