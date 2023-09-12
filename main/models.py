from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255) #batas panjang max panjang nama = 255 karakter
    amount = models.IntegerField() #menyimpan bilangan bulat
    description = models.TextField() #buat teks dengan panjang variabel