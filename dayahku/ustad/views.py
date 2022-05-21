#vies app ustad
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import InputTugas, InputMateri
from .models import Tugas, Materi

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



def siswa(request):
    return render(request, 'ustad/siswa.html')

def tambahmateri(request):
    submited = False
    form = InputMateri(request.POST,request.FILES)

    print(request.POST)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect("/loginUstad/kelas/materi")
        else:
            print(form.errors.as_data())
    else:
        form = InputMateri
        if "submited" in request.GET:
            submited = True
    
    return render(request, 'ustad/tambahmateri.html', {'form': form})

def materi(request):
    daftar_materi = Materi.objects.all()
    return render(request, 'ustad/materi.html', {'daftar_materi' : daftar_materi})

def tugas(request):
    daftar_tugas = Tugas.objects.all()
    return render(request, 'ustad/tugas.html', {'daftar_tugas' : daftar_tugas})

def tambahtugas(request):
    submited = False
    form = InputTugas(request.POST,request.FILES)

    print(request.POST)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect("/loginUstad/kelas/tugas")
        else:
            print(form.errors.as_data())
    else:
        form = InputTugas
        if "submited" in request.GET:
            submited = True
    
    return render(request, 'ustad/tambahtugas.html', {'form': form})

def tambahsiswa(request):
     return render(request, 'ustad/tambahsiswa.html')