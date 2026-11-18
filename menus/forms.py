from django import forms
from .models import MenuItem, Restaurant


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ["name"]
        labels = {"name": "Name"}


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["category", "name", "description", "price"]
        labels = {
            "category": "Category",
            "name": "Name",
            "description": "Description",
            "price": "Price",
        }
        widgets = {
            "price": forms.NumberInput(attrs={"step": "0.01", "min": "0"}),
        }
