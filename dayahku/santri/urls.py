#urls di app santri

from django.urls import path
from . import views

urlpatterns =[
    path('',views.login),

]