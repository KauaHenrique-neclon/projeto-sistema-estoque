from django.urls import path
from app.views import viewsUsuario

urlpatterns = [
    path('usuario',viewsUsuario.index, name='usuario'),
]
