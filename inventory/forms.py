from django import forms
from .models import Item, Supplier

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        labels = {
            'code': 'Code',
            'title': 'Title',
            'supplier': 'Supplier',
            'link': 'Link',
            'slot': 'Slot',
            'price': 'Price',
            'amount': 'Amount'
        }
        widgets = {
            'code': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
            'slot': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'})
        }