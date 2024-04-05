from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Item, Supplier

from .forms import ItemForm, SupplierForm

from django.db.models import Q

from django.core.paginator import Paginator

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Item
import json


@csrf_exempt
def update_item_amount(request, id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item = Item.objects.get(pk=id)
            item.amount = data.get('amount')
            item.save()
            return JsonResponse({'success': True})
        except Item.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Item not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


def index(request):
    query = request.GET.get('q')
    if query:
        items_list = Item.objects.filter(Q(title__istartswith=query) | Q(code__istartswith=query))
    else:
        items_list = Item.objects.all()

    paginator = Paginator(items_list, 6)  # Show 5 items per page
    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)

    return render(request, 'inventory/index.html', {
        'items': items
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


def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            new_supplier_name = form.cleaned_data['name']
            new_supplier_address = form.cleaned_data['address']
            new_supplier_contact_person = form.cleaned_data['contact_person']
            new_supplier_phone = form.cleaned_data['phone']
            new_supplier_email = form.cleaned_data['email']
            new_supplier_website = form.cleaned_data['website']

            new_supplier = Supplier(
                name=new_supplier_name,
                address=new_supplier_address,
                contact_person=new_supplier_contact_person,
                phone=new_supplier_phone,
                email=new_supplier_email,
                website=new_supplier_website
            )
            new_supplier.save()
            return render(request, 'inventory/add_supplier.html', {
                'form': SupplierForm(),
                'success': True
            })
    else:
        form = SupplierForm()
    return render(request, 'inventory/add_supplier.html', {
        'form': SupplierForm()
    })


def edit_item(request, id):
    item = Item.objects.get(pk=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ItemForm(instance=item)
    return render(request, 'inventory/edit_item.html', {
        'form': form,
        'item': item
    })


def edit_supplier(request, id):
    supplier = Supplier.objects.get(pk=id)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'inventory/edit_supplier.html', {
        'form': form,
        'supplier': supplier
    })


def delete_item(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('index'))
