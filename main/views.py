from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Silakan masukkan barang yang ingin disimpan 🥂',
        'amount': 'Masukkan jumlah barang yang akan disimpan (jumlah barang harus berupa bilangan bulat)',
        'description' : 'StokNya Aku adalah sebuah web yang dapat menyimpan dan membantumu memantau jumlah barang-barang kesayanganmu 💞'
    }

    return render(request, "main.html", context)