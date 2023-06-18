from django import forms
from django.forms import ModelForm

from organizationalAPP.models import Clothes, ClothType, ClothSubType, Sizes


class ClothesForm(ModelForm):
    """Form do edycji ubrania"""
    class Meta:
        model = Clothes
        fields = (
            "name", "brand", "size", "purchase_price",
            "predicted_sale_price", "sold_price", "condition", "cloth_type",
            "cloth_sub_type", "description", "marketplaces", "photo",
            'sell_statute',
            )


class EditTypeSizesForm(ModelForm):
    """Form do edycji rozmiarów w typie"""
    class Meta:
        model = ClothType
        fields = ("measurement",)


class AddForm(forms.ModelForm):
    """Form dodania nowego ubrania"""

    class Meta:
        model = Clothes
        fields = (
            "name", "brand", "size", "purchase_price",
            "predicted_sale_price", "condition", "cloth_type", "cloth_sub_type",
            "description", "marketplaces", "photo"
            )

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "brand": forms.TextInput(attrs={"class": "form-control"}),
            "size": forms.Select(attrs={"class": "form-control"}),
            "cloth_type": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Name"
        self.fields["brand"].label = "Brand"
        self.fields["size"].label = "Size"
        self.fields["description"].label = "Description"
        self.fields["photo"].label = "Photo"


class AddTypeForm(forms.ModelForm):
    """Form dodania nowego typu ubrania"""

    class Meta:
        model = ClothType
        fields = ("type",)

        widgets = {"type": forms.TextInput(attrs={"class": "form-control"})}

    def __init__(self, *args, **kwargs):
        super(AddTypeForm, self).__init__(*args, **kwargs)
        self.fields["type"].label = "New type"


class AddSubTypeForm(forms.ModelForm):
    """Form dodania nowego sub-typu ubrania"""

    class Meta:
        model = ClothSubType
        fields = ("type",)

        widgets = {"type": forms.TextInput(attrs={"class": "form-control"})}

    def __init__(self, *args, **kwargs):
        super(AddSubTypeForm, self).__init__(*args, **kwargs)
        self.fields["type"].label = "New sub-type"

class AddMeasurementsForm(forms.ModelForm):
    """Form dodania wymiaru ubrania"""

    class Meta:
        model = Sizes
        fields = ("type",)

        widgets = {"type": forms.TextInput(attrs={"class": "form-control"})}

    def __init__(self, *args, **kwargs):
        super(AddMeasurementsForm, self).__init__(*args, **kwargs)
        self.fields["type"].label = "New measurements"

