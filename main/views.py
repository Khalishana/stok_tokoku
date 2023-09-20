from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

from main.models import Item

# Create your views here.
def show_main(request):
    products = Item.objects.all() #buat ngambil semua object item yang disimpen di database
    product_count = products.count() #menghitung jumlah produk yang ada di stok

    context = {
        'name': 'Silakan masukkan barang yang ingin disimpan 🥂',
        'amount': 'Masukkan jumlah barang yang akan disimpan (jumlah barang harus berupa bilangan bulat)',
        'description' : 'StokNya Aku adalah sebuah web yang dapat menyimpan dan membantumu memantau jumlah barang-barang kesayanganmu 💞',
        'products': products,
        'product_count': product_count
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST": #validasi isi form
        form.save() #menyimpan data dari form
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request): #nampilin code dalam bentuk xml
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request): #nampilin code dalam bentuk json
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")