from django import forms

from .models import Menu


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = [
            'hidden',
            'name',
            'alternateName',
            'code',
            'sku',
            'price',
            'unitName',
            'cost',
            'isRevenue',
            'itemGroup',
            'priceType',
            'taxRate',
            'canonical',
            'itemStock',
            'options',
        ]
