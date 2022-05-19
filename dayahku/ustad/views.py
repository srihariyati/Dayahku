#vies app ustad
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'ustad/login.html')
def kelas(request):
    return render(request, 'ustad/kelas.html')