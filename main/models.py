from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255) #batas panjang max panjang nama = 255 karakter
    #date_added = models.DateField(auto_now_add=True) #add tanggal sekarang
    amount = models.IntegerField() #menyimpan bilangan bulat
    description = models.TextField() #buat teks dengan panjang variabel
    date_added = models.DateField(auto_now_add=True) #add tanggal sekarang