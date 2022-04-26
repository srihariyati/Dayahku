#views app santri
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'santri/login.html')
