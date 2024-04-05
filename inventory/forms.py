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


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        labels = {
            'name': 'Name',
            'address': 'Address',
            'contact_person': 'Contact Person',
            'phone': 'Phone',
            'email': 'Email',
            'website': 'Website'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'})
        }