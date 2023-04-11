from django import forms
from django.forms import ModelForm, SelectDateWidget

from organizationalAPP.models import Clothes, ClothType


class ClothesForm(ModelForm):
    class Meta:
        model = Clothes
        fields = ['name', 'brand', 'size', 'description', 'photo']


class AddForm(forms.ModelForm):
    """Form dodania nowego ubrania"""


    class Meta:
        model = Clothes
        fields = ('name', 'brand', 'size', 'cloth_type', 'description', 'photo')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
            'cloth_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nazwa"
        self.fields['brand'].label = "Marka"
        self.fields['size'].label = "Rozmiar"
        self.fields['description'].label = "Opis"
        self.fields['photo'].label = "Zdjęcie"


class AddTypeForm(forms.ModelForm):
    """Form dodania nowego typu ubrania"""


    class Meta:
        model = ClothType
        fields = ('type', )

        widgets = {
            'type': forms.TextInput(attrs={'class': 'form-control'})
            }

    def __init__(self, *args, **kwargs):
        super(AddTypeForm, self).__init__(*args, **kwargs)
        self.fields['type'].label = "Nowy typ ubrania"