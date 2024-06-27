from django.db import models

class Buku(models.Model):
    judul= models.CharField(max_length= 245)
    deskripsi= models.TextField()
    author = models.CharField(max_length= 254)
    tahun = models.CharField(max_length= 50)