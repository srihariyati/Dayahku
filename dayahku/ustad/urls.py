#urls di app ustad

from django.urls import path
from ustad import views

urlpatterns =[
    path('',views.loginView),
    path('kelas/',views.kelas),
    path('kelas/materi/',views.materi),
    path('kelas/tugas/',views.tugas),
    path('kelas/siswa/',views.siswa),
    path('kelas/tugas/tambahtugas',views.tambahtugas),
    path('kelas/materi/tambahmateri',views.tambahmateri),
    path('kelas/siswa/tambahsiswa',views.tambahsiswa),


]