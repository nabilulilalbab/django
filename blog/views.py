from django.shortcuts import render
from .models import Artikel
# Create your views here.
def index(request):
    articles = Artikel.objects.all()
    category = Artikel.objects.values('kategori__nama').distinct()
    context = {
        'Judul' : 'Blog',
        'Heading' : 'Ini adalah halaman Blog',
        'Articles' : articles,
        'Categories' : category,
    }
    return render(request,'blog/index.html',context)

def detail_artikel(request,slugInput):
    detail_articles = Artikel.objects.get(slug_art=slugInput)
    context = {
        'Judul' : 'Detail Blog',
        'Heading' : 'Ini detail Blog',
        'DetailArtikel' : detail_articles,
    }
    return render(request,'blog/detail.html',context)

def kategori_artikel(request,kategoriInput):
    articles = Artikel.objects.filter(kategori__nama=kategoriInput)
    category = Artikel.objects.values('kategori__nama').distinct()
    context = {
        'Judul' : 'kategori Blog',
        'Heading' : 'Ini halaman berdasarkan kategori Blog',
        'Artikel' : articles,
        'Categories' : category,
    }
    return render(request,'blog/kategori.html',context)