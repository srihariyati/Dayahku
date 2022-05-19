#urls di app santri

from django.urls import path
from . import views

urlpatterns =[
    path('',views.login),
    path('materi/',views.materi),
    path('tugas/',views.tugas),
]