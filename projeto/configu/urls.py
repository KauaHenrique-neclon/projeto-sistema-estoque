from django.contrib import admin
from django.urls import path, include
from app.urls.urls import urlpatterns as urlestoque
from app.urls.urlsCompra import urlpatterns as urlCompras
from app.urls.urlsUsuario import urlpatterns as urlUsuario
from app.urls.urlsEmpresa import urlpatterns as urlEmpresa
from app.urls.urlsDashboard import urlpatterns as urlDashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(urlestoque)),
    path('compras/',include(urlCompras)),
    path('usuario/',include(urlUsuario)),
    path('empresa/',include(urlEmpresa)),
    path('dashboard/',include(urlDashboard)),
]