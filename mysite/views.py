from django.shortcuts import render

def index(request):
    context = {
        'Judul' : 'Home',
        'Heading' : 'selamat datang di Home'
    }
    return render(request,'index.html',context)