from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse

from main.models import Item

# Create your views here.
def show_main(request):
    products = Item.objects.all() #buat ngambil semua object item yang disimpen di database

    context = {
        'name': 'Silakan masukkan barang yang ingin disimpan 🥂',
        'amount': 'Masukkan jumlah barang yang akan disimpan (jumlah barang harus berupa bilangan bulat)',
        'description' : 'StokNya Aku adalah sebuah web yang dapat menyimpan dan membantumu memantau jumlah barang-barang kesayanganmu 💞',
        #'date': 'web ini melakukan update secara real-time sesuai tanggal input item',
        'products': products
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST": #validasi isi form
        form.save() #menyimpan data dari form
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)