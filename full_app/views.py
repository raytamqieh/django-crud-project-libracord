from django.shortcuts import render, redirect
from .models import Buku
from .forms import BukuForm

def welcome(request):
    return render(request, "welcome.html")

def load_form(request):
    form = BukuForm
    return render(request, 'index.html', {'form':form})

def add(request):
    form =BukuForm(request.POST)
    form.save()
    return redirect('/show')

def show(request):
    buku = Buku.objects.all 
    return render(request, 'show.html', {'buku':buku})

def edit(request, id):
    buku = Buku.objects.get(id=id)
    return render(request, 'edit.html', {'buku':buku})

def update(request, id):
    buku = Buku.objects.get(id=id)
    form = BukuForm(request.POST, instance=buku)
    form.save()
    return redirect('/show') 

def delete(request, id):
    buku = Buku.objects.get(id=id)
    buku.delete()
    return redirect('/show') 


def search(request):
    given_name = request.POST['name']
    buku = Buku.objects.filter(judul__icontains = given_name)
    return render(request, 'show.html', {'buku':buku})