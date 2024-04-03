from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Item, Supplier

from .forms import ItemForm


# Create your views here.
def index(request):
    return render(request, 'inventory/index.html', {
        'items': Item.objects.all()
    })

def view_item(request, id):
    item = Item.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            new_item_number = form.cleaned_data['code']
            new_item_title = form.cleaned_data['title']
            new_item_supplier = form.cleaned_data['supplier']
            new_item_link = form.cleaned_data['link']
            new_item_slot = form.cleaned_data['slot']
            new_item_price = form.cleaned_data['price']
            new_item_amount = form.cleaned_data['amount']

            new_item = Item(
                code=new_item_number,
                title=new_item_title,
                supplier=new_item_supplier,
                link=new_item_link,
                slot=new_item_slot,
                price=new_item_price,
                amount=new_item_amount
            )
            new_item.save()
            return render(request, 'inventory/add_item.html', {
                'form': ItemForm(),
                'success': True
            })
    else:
        form = ItemForm()
    return render(request, 'inventory/add_item.html', {
        'form': ItemForm()
    })