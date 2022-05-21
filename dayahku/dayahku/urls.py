from django.contrib import admin
from xml.etree.ElementInclude import include
from django.urls import include, path

import santri

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('santri.urls')),
    path('loginUstad/', include('ustad.urls')),
    path('kelas/', include('ustad.urls')),
    path('materi/',include('ustad.urls')),
    path('tugas/',include('ustad.urls')),
    path('siswa/',include('ustad.urls')),
    path('tambahtugas/',include('ustad.urls')),
    path('tambahmateri/',include('ustad.urls')),

    path('materi/', include('santri.urls')),
    path('tugas/', include('santri.urls')),
    path('deskripsitugas/',include('santri.urls')),
    

]
