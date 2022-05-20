#urls di app santri

from django.urls import path
from santri import views

urlpatterns =[
    path('',views.loginView),
    path('materi/',views.materi),
    path('tugas/',views.tugas),
]