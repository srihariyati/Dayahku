#vies app ustad
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import PostForm

# Create your views here.
def loginView(request):
    if request.method == "POST":
        print(request.POST)
        username_login = request.POST['username']
        password_login = request.POST['password']
        
        user = authenticate(request, username=username_login, password=password_login)
        print(user)

        if user is not None:
           login(request, user)
           return redirect('kelas/')
        else:
            return redirect('/loginUstad')
       
    return render(request,'ustad/login.html')

def kelas(request):
    return render(request, 'ustad/kelas.html')

def materi(request):
    return render(request, 'ustad/materi.html')

def tugas(request):
    return render(request, 'ustad/tugas.html')


def siswa(request):
    return render(request, 'ustad/siswa.html')

def tambahmateri(request):
    return render(request, 'ustad/tambahmateri.html')

def tambahtugas(request):
    post_form = PostForm()

    if request.method =='POST':
        print(request.POST)

    context={
        'post_form' : post_form

    }
    return render (request , 'ustad/tambahtugas.html', context)

