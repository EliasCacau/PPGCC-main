from django.urls import path
from usuario.views import *

urlpatterns = [
    path("usuario/", usuario),
    path("cadastro_usuario/", cadastro),
    path("criar_usuario/", criar_usuario)
]
