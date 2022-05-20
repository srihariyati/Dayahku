#urls di app ustad

from django.urls import path
from ustad import views

urlpatterns =[
    path('',views.loginView),
    path('kelas/',views.kelas),

]