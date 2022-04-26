from xml.etree.ElementInclude import include
from django.urls import include, path

urlpatterns = [
    path('', include('santri.urls')),
    path('loginUstad/', include('ustad.urls')),

]
