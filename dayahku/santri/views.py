#views app santri
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def loginView(request):
    if request.method == "POST":
        print(request.POST)
        username_login = request.POST['username']
        password_login = request.POST['password']
        
        user = authenticate(request, username=username_login, password=password_login)
        print(user)

        if user is not None:
           login(request, user)
           return redirect('/materi')
        else:
            return redirect('/')
       

    return render(request,'santri/login.html')

def materi(request):
    return render(request,'santri/materi.html')

def tugas(request):
    return render(request,'santri/tugas.html')

def deskTugas(request):
    return render(request, 'santri/deskripsi_tugas.html')

def download_materi(request):
    return render(request, 'santri/download_materi.html')