from django import forms
from django.forms import ModelForm, SelectDateWidget

from organizationalAPP.models import Clothes


class ClothesForm(ModelForm):
    class Meta:
        model = Clothes
        fields = ['name', 'brand', 'size', 'description', 'photo']


class AddForm(forms.ModelForm):
    """Form dodania nowego ubrania"""

    # name = forms.CharField(label='Nazwa')
    # brand = forms.CharField(label='Marka')
    # size = forms.ChoiceField(label='Rozmiar')
    # description = forms.CharField(label='Opis')

    class Meta:
        model = Clothes
        fields = ('name', 'brand', 'size', 'description', 'photo')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nazwa"
        self.fields['brand'].label = "Marka"
        self.fields['size'].label = "Rozmiar"
        self.fields['description'].label = "Opis"
        self.fields['photo'].label = "Zdjęcie"

