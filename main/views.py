from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.shortcuts import get_object_or_404 #buat cegah error pas mau ngambil/nambah amount dari database

from main.models import Item

# Create your views here.
@login_required(login_url='/login') #biar main cuma bisa diakses sama user yang udah login
def show_main(request):
    #products = Item.objects.all() #buat ngambil semua object item yang disimpen di database
    products = Item.objects.filter(user=request.user)
    product_count = products.count() #menghitung jumlah produk yang ada di stok

    context = {
        #'name': 'Silakan masukkan barang yang ingin disimpan 🥂',
        'name': request.user.username,
        'amount': 'Masukkan jumlah barang yang akan disimpan (jumlah barang harus berupa bilangan bulat)',
        'description' : 'StokNya Aku adalah sebuah web yang dapat menyimpan dan membantumu memantau jumlah barang-barang kesayanganmu 💞',
        'products': products,
        'product_count': product_count,
        'last_login': request.COOKIES['last_login'], #nambahi informasi last login
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST": #validasi isi form
        product = form.save(commit=False) #biar objek ga langsung disimpen di database
        product.user = request.user
        #form.save() #menyimpan data dari form
        product.save()
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

def register(request): #buat registrasi akun
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Selamat! akun kamu berhasil dibuat 🤩")
            return redirect('main:login') #abis berhasil buat akun bakal balik ke laman login
    context = {'form':form}
    return render(request, 'register.html', context)
    
def login_user (request):
    if request.method == "POST":
        username = request.POST.get('username') #minta input username
        password = request.POST.get('password') #minta input password
        pengguna = authenticate(request, username=username, password=password) #cek apakah username dan password udah sesuai
        if pengguna is not None:
            login(request, pengguna)
            #return redirect('main:show_main') #kalo pengguna ada, direct ke laman utama
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else: #kalo username atau password ga sesuai
            messages.info(request, 'Oh tidak username atau password yang kamu masukkan salah 😱😱. Gapapa, silakan coba lagi 🙆‍♀️')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login') #hapus cookie kapan last login
    return response #kl user logout, balik ke laman login

def tambah_amount(request, id): #method buat tambah produk
    product = get_object_or_404(Item, pk=id)

    #tambah 1 produk
    product.amount += 1
    product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def kurangi_amount(request, id):
    product = get_object_or_404(Item, pk=id) #ga perlu pake request karena cuma ngurangin amount

    #kurangi 1 produk selama jumlah item lebih dari 0
    if product.amount > 0:
        product.amount -= 1
        product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def delete_item(request, id): #fungsi delete item
    #product = Item.objects.get(pk=id)
    if request.method == "POST":
        product = get_object_or_404(Item, pk=id)
        product.delete()
        #return HttpResponse(reverse('main:show_main'))
        return redirect('main:show_main')