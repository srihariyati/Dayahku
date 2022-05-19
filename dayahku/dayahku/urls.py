from xml.etree.ElementInclude import include
from django.urls import include, path

urlpatterns = [
    path('', include('santri.urls')),
    path('loginUstad/', include('ustad.urls')),
    path('kelas/', include('ustad.urls')),

    path('materi/', include('santri.urls')),
    path('tugas/', include('santri.urls')),
    

]
