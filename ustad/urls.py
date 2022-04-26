#urls di app ustad

from django.urls import path
from . import views

urlpatterns =[
    path('',views.login),

]