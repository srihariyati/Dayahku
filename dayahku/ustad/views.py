#vies app ustad
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'ustad/login.html')