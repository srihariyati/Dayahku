#urls di app santri

from django.urls import path
from santri import views

urlpatterns =[
    path('',views.loginView),
    path('materi/',views.materi),
    path('download_materi/',views.download_materi),
    path('tugas/',views.tugas),
    path('deskripsitugas/',views.deskTugas),
]